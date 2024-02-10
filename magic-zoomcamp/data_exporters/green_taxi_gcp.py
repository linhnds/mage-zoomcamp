import pyarrow as pa
import pyarrow.parquet as pq
import os


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/main-shade-395414-2463a78bca4f.json'

@data_exporter
def export_data_to_google_cloud_storage(data, *args, **kwargs) -> None:
    project_id = kwargs['project_id']
    bucket_name = kwargs['bucket_name']
    table_name = kwargs['table_name']
    root_path = f"{bucket_name}-{project_id}/{table_name}"
    print(root_path)
    partition_cols = kwargs['partition_cols']

    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=partition_cols,
        filesystem=gcs
    )
