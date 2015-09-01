# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:01:07 2015

@author: Graham
"""

import sqlite3 as lite
import pandas as pd
import pandas.io.sql as psql

""" Connect to the database """
con = lite.connect('C:\Users\Graham\Documents\Thinkful Data Science\Unit 1\SQLite\getting_started.db')
cur = con.cursor()

populate_cities = """
INSERT INTO cities (name, state) VALUES
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA');
"""
populate_weather = """
INSERT INTO weather (city,year,warm_month,cold_month,average_high) VALUES
    ('New York City',2013,'July','January',62),
    ('Boston',2013,'July','January',59),
    ('Chicago',2013,'July','January',59),
    ('Miami',2013,'August','January',84),
    ('Dallas',2013,'July','January',77),
    ('Seattle',2013,'July','January',61),
    ('Portland',2013,'July','December',63),
    ('San Francisco',2013,'September','December',64),
    ('Los Angeles',2013,'September','December',75);
"""


""" Create the cities and weather tables """
cur.execute("DROP TABLE IF EXISTS cities")
cur.execute("CREATE TABLE cities (name text, state text)")
cur.execute("DROP TABLE IF EXISTS weather")
cur.execute("CREATE TABLE weather (city text,year integer,warm_month text,cold_month text,average_high integer)")

""" Populate the tables """
cur.execute(populate_weather)
cur.execute(populate_cities)