from google.cloud import bigquery
from pgsql import _query
import requests
import json
import sql

if __name__ == '__main__':
    #_query(sql.create_schema)  # create new schema in pgadmin "petl3"
    #_query(sql.create_table, [])

    client = bigquery.Client() # do i need a project name????
    query = client.query(
        """
        SELECT *
        FROM `bigquery-public-data.stackoverflow.posts_questions`
        ORDER BY view_count DESC
        LIMIT 10;
        
        with cte_median AS (
        SELECT median_rent, median_age, geo_id
	    FROM bigquery-public-data.census_bureau_acs.county_2017_1yr
        where median_rent < 2000 AND median_age < 30 
        ),

        cte_mobilty_data AS (
        SELECT census_fips_code AS code, 
            sub_region_1 AS state, sub_region_2 AS county, AVG(retail_and_recreation_percent_change_from_baseline) AS sales_vector
        from bigquery-public-data.covid19_google_mobility.mobility_report 
        where  retail_and_recreation_percent_change_from_baseline IS NOT NULL 
        group by code, sub_region_1, sub_region_2
        having sales_vector > -15 
        )

        SELECT c.geo_id, state, county, sales_vector 
        from cte_median AS c
        JOIN cte_mobilty_data AS m
        ON c.geo_id||'.0' = m.code
        """
    )
    for row in query.result():
        _query(sql.insert_data, [int(row[0]), row[1], row[2], int(row[3])])
#        print(row)


#    for row in query.result():
