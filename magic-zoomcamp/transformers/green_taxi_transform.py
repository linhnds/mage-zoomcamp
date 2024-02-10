if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):    
    # Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero.
    print(f"Original shape: {data.shape}")
    df = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    print(f"After filter: {df.shape}")

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date
    df['lpep_dropoff_date'] = df['lpep_dropoff_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    new_columns = df.columns.str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
    edited_columns = df.columns.difference(new_columns)
    print(f"There are {len(edited_columns)} edited column names: {edited_columns.values}")
    df.columns = new_columns.str.lower()
    print(f"New column names: {df.columns.values}")

    # Add three assertions:
    # vendor_id is one of the existing values in the column (currently)
    print(f"Unique values of vendor_id: {list(df['vendor_id'].unique())}")

    # passenger_count is greater than 0
    print(f"Number of rows with passenger_count <= zero: {len(df[df['passenger_count'] <= 0])}")
    # trip_distance is greater than 0
    print(f"Number of rows with trip_distance <= zero: {len(df[df['trip_distance'] <= 0])}")

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
