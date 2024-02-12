if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data['lpep_pickup_datetime'] = data['lpep_pickup_datetime'].dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    data['lpep_dropoff_datetime'] = data['lpep_dropoff_datetime'].dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    print(data.dtypes)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
