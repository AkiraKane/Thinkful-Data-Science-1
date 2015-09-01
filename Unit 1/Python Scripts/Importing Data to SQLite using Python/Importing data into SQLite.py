# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 19:58:00 2015

@author: Graham
"""

import sqlite3 as lite
import pandas as pd

con = lite.connect('C:\\Users\\Graham\\Documents\\Thinkful Data Science\\Unit 1\\SQLite\\getting_started.db')

# Inserting rows by passing values directly to `execute()`
with con:

    cur = con.cursor()
    cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
    cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
    cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January', 47)")
    cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', 78)")
    cur.execute("INSERT INTO weather VALUES('Boston', 2013, 'July', 'January', 59)")
    cur.execute("INSERT INTO weather VALUES('Chicago', 2013, 'July', 'January', 59)")
    cur.execute("INSERT INTO weather VALUES('Miami', 2013, 'August', 'January', 84)")
    cur.execute("INSERT INTO weather VALUES('Dallas', 2013, 'July', 'January', 77)")
    cur.execute("INSERT INTO weather VALUES('Seattle', 2013, 'July', 'January', 61)")
    cur.execute("INSERT INTO weather VALUES('Portland', 2013, 'July', 'December', 63)")
    cur.execute("INSERT INTO weather VALUES('San Francisco', 2013, 'September', 'December', 64)")
    cur.execute("INSERT INTO weather VALUES('Los Angeles', 2013, 'September', 'December', 75)")
    con.commit()

with con:
    
    cur = con.cursor()
    cur.execute("SELECT * FROM weather")
    
    
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
   
    print df
    
    """how do I get both tables into one dataframe?"""