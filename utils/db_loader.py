import csv, sqlite3
import uuid

"""
CREATE TABLE "catalog_geonames" 
    ("id" char(32) NOT NULL PRIMARY KEY, 
    "country_code" varchar(2) NOT NULL, 
    "postal_code" varchar(20) NOT NULL, 
    "place_name" varchar(200) NOT NULL, 
    "state_code" varchar(20) NULL, 
    "state_name" varchar(100) NULL
    "county_name" varchar(100) NULL, 
    "county_code" varchar(20) NULL, 
    "community_name" varchar(100) NULL, 
    "community_code" varchar(20) NULL, 
    "latitude" real NULL, "longitude" real NULL,
    );
"""
con = sqlite3.connect("../db.sqlite3")
cur = con.cursor()
#cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

with open('data/IN.txt','rb') as datafile: # `with` statement available in 2.5+
    fieldnames=['country_code', 'postal_code', 'place_name', 'state_name','state_code'
        "couny_name", "county_code", "community_name", "community_code", "latitude", "longitude"]
    csvreader = csv.DictReader(datafile, fieldnames=fieldnames, delimiter='\t') # comma is default delimiter
    records = [(str(uuid.uuid4()), i[0], i[1], i[2], i[3], i[4], i[5], 
                i[6], i[7], i[8], i[9]) for i in csvreader]
    for record in records:
        print(record)
"""
cur.executemany("INSERT INTO t (id, country_code, postal_code, palce_name, state_name, state_code,
                county_name, county_code, community_name, community_code, latitude, longitude ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", records)
con.commit()
con.close()
"""
