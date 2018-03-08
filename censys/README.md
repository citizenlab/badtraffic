This directory contains a **summary** of data collected with [censys](censys.io). Censys is 
a platform that allows security researchers to access current and historical data on publicly
available ip, and certificate data.  

Presented here is a summary of aggregate result counts found on Censys in the course of 
this research.  We used Censys to find all cases where redirections were being made to the
static.dbmads[ . ]com domain.  

To do this we ran the following query against the Censys historical ipv4 dataset
through BigQuery.  We used the following base query:

```
#standardSQL
SELECT
 distinct(ip),
 p80.http.get.headers.location p80loc,
 p8080.http.get.headers.location p8080loc,
 p8888.http.get.headers.location p8888loc,
 p7547.cwmp.get.headers.location p7547loc
FROM
 `censys-io.ipv4_public.20180104`
WHERE
 p80.http.get.headers.location LIKE '%static.dbmads.com%'
 or
 p8080.http.get.headers.location LIKE '%static.dbmads.com%'
 or 
 p7547.cwmp.get.headers.location LIKE '%static.dbmads.com%'
 or
 p8888.http.get.headers.location LIKE '%static.dbmads.com%'
;
```

We then did this against all tables and annotated the result in
```censys-summary.csv``` and noted how many rows were returned 
in the ```result_ct``` column.  Since there are schema changes 
in the whole data set we noted any such changes in the ```notes```
column.



