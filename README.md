## SETUP

### Question 1:
What is count of records for the 2022 Green Taxi Data?
```
select
  count(*)
from
  mage_zoomcamp_m3.external_green_tripdata;
```

### Question 2:
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
```
select
  count(distinct PULocationID)
from
  mage_zoomcamp_m3.external_green_tripdata;
```
```
select
  count(distinct PULocationID)
from
  mage_zoomcamp_m3.green_tripdata_non_partitioned;
```


### Question 3:
How many records have a fare_amount of 0?
```
select
  count(*)
from mage_zoomcamp_m3.external_green_tripdata
where fare_amount = 0;
```


### Question 4:
What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)
```
CREATE OR REPLACE TABLE mage_zoomcamp_m3.green_tripdata_partitoned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT * FROM mage_zoomcamp_m3.external_green_tripdata;
```

### Question 5:
Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)
```
select distinct(PULocationID)
from mage_zoomcamp_m3.green_tripdata_non_partitioned
where date(lpep_pickup_datetime) between '2022-01-06' and '2022-06-30';
```
```
select distinct(PULocationID)
from mage_zoomcamp_m3.green_tripdata_partitoned_clustered
where date(lpep_pickup_datetime) between '2022-01-06' and '2022-06-30';
```