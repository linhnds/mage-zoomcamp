import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    year = kwargs['year']
    months = kwargs['months']
    file_type = kwargs['file_type']
    df = pd.DataFrame()
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID':pd.Int64Dtype(),
        'store_and_fwd_flag':str,
        'PULocationID':pd.Int64Dtype(),
        'DOLocationID':pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra':float,
        'mta_tax':float,
        'tip_amount':float,
        'tolls_amount':float,
        'improvement_surcharge':float,
        'total_amount':float,
        'congestion_surcharge':float
    }
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    for month in months:
        if file_type == 'csv':
            base_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green"
            file_name = f"green_tripdata_{year}-{month:02d}.csv.gz"
            url = f'{base_url}/{file_name}'
            df_month = pd.read_csv(
                url,
                sep=',',
                compression='gzip',
                dtype=taxi_dtypes,
                parse_dates=parse_dates
            )
        else:
            base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data"
            file_name = f"green_tripdata_{year}-{month:02d}.parquet"
            url = f"{base_url}/{file_name}"
            df_month = pd.read_parquet(url)
        print(f"Month {month:02d}: {len(df_month):,}")
        df = pd.concat([df, df_month], axis=0)
    print(f"Total rows: {len(df):,}")
    print(df.dtypes)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
