# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:25:56 2015

@author: Graham
"""

import sqlite3 as lite
import pandas as pd
import pandas.io.sql as psql

"""Connect to db"""
con = lite.connect('C:\\Users\\Graham\\Documents\\Thinkful Data Science\\Unit 1\\SQLite\\test4.db')
cur = con.cursor()

populate_cities = """
INSERT INTO cities (name, state) VALUES
    ('New York City', 'NY');
"""

populate_weather = """
INSERT INTO weather (city, year, warm_month, cold_month, average_high) VALUES
    ('New York City', 2013, 'July', 'January', 62);
"""

""" Create the cities and weather tables """
cur.execute("DROP TABLE IF EXISTS cities")
cur.execute("CREATE TABLE cities (name text, state text)")
cur.execute("DROP TABLE IF EXISTS weather")
cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")

""" Populate the tables """
cur.execute(populate_weather)
cur.execute(populate_cities)
con.commit()