#create new schema
create_schema = ('''
    create schema IF NOT EXISTS petl3;
''')
#create new table for petl3
create_table = ('''
    DROP TABLE IF EXISTS petl3.vaible_countys;
    CREATE TABLE IF NOT EXISTS petl3.viable_countys (
        geo_id INT,
        state TEXT,
        county TEXT,
        sales_vector INT
        )
''')

insert_data = ('''
    INSERT INTO petl3.viable_countys (geo_id, state, county, sales_vector) 
        VALUES(%s, %s, %s, %s)
''')