# SETUP
<p>Create an external table using the Green Taxi Trip Records Data for 2022.</p>
```
CREATE OR REPLACE EXTERNAL TABLE `mage_zoomcamp_m3.external_green_tripdata`
OPTIONS (
format = 'PARQUET',
uris = ['gs://mage-zoomcamp-m3-main-shade-395414/green_taxi_data-2022/*.parquet']
);
```
<p>Create a table in BQ using the Green Taxi Trip Records for 2022 (do not partition or cluster this table).</p>
```
CREATE OR REPLACE TABLE `mage_zoomcamp_m3.green_tripdata_non_partitioned` AS
SELECT * FROM `mage_zoomcamp_m3.external_green_tripdata`;
```
