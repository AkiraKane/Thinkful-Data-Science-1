# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:57:08 2015

@author: Graham
"""


"""
Write a script called "database.py" to print out the cities with the July being the warmest month. 
Your script must:

Connect to the database
Create the cities and weather tables (HINT: first pass the statement DROP TABLE IF EXISTS <table_name>; to remove the table before you execute the CREATE TABLE ... statement)
Insert data into the two tables
Join the data together
Load into a pandas DataFrame
Print out the resulting city and state in a full sentence. For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."
Push your code to Github and enter the link below
"""


import sqlite3 as lite
import pandas as pd

con = lite.connect('C:\\Users\\Graham\\Documents\\Thinkful Data Science\\Unit 1\\SQLite\\SevenSummits.db')

with con:
    
    cur = con.cursor()
    
    'checking if the tables exists, deleting if yes'
    cur.execute("DROP TABLE IF EXISTS mountains")
    cur.execute("DROP TABLE IF EXISTS summits")
    con.commit()
    
    'creating and populating table: Mountains'
    cur.execute("CREATE TABLE mountains (Mountain text, Continent Text, Height float)")
    cur.execute("INSERT INTO mountains VALUES('Mount McKinley (Denali)', 'North America', 6168)")    
    cur.execute("INSERT INTO mountains VALUES('Aconcagua', 'South America', 6960.8)") 
    cur.execute("INSERT INTO mountains VALUES('Vinson Massif', 'Antartica', 4892)") 
    cur.execute("INSERT INTO mountains VALUES('Mount Kilimanjaro', 'Africa', 5895)") 
    cur.execute("INSERT INTO mountains VALUES('Mount Everest', 'Asia', 8848)") 
    cur.execute("INSERT INTO mountains VALUES('Puncak Jaya', 'Austrailia', 4884)") 
    cur.execute("INSERT INTO mountains VALUES('Mount Blanc', 'Europe', 4810)") 
    cur.execute("INSERT INTO mountains VALUES('Mount Elbrus', 'Europe', 5642)")
    con.commit()
    
    'creating and populating table: Summits'
    cur.execute("CREATE TABLE summits (Person text, Mountain text, Year int)")
    cur.execute("INSERT INTO summits VALUES('Hudson Stuck', 'Mount McKinley (Denali)', 1913)")
    cur.execute("INSERT INTO summits VALUES('Harry Karstens', 'Mount McKinley (Denali)', 1913)")
    cur.execute("INSERT INTO summits VALUES('Walter Harper', 'Mount McKinley (Denali)', 1913)")
    cur.execute("INSERT INTO summits VALUES('Matthias Zurbriggen', 'Aconcagua', 1897)")
    cur.execute("INSERT INTO summits VALUES('Group of Four', 'Vinson Massif', 1966)")
    cur.execute("INSERT INTO summits VALUES('Hans Meyer', 'Mount Kilimanjaro', 1889)")
    cur.execute("INSERT INTO summits VALUES('Ludwig Purtscheller', 'Mount Kilimanjaro', 1889)")
    cur.execute("INSERT INTO summits VALUES('Tenzing Norgay', 'Mount Everest', 1953)")
    cur.execute("INSERT INTO summits VALUES('Edmund Hillary', 'Mount Everest', 1953)")
    cur.execute("INSERT INTO summits VALUES('Heinrich Harrer', 'Puncak Jaya', 1962)")
    cur.execute("INSERT INTO summits VALUES('F. Crauford Grove', 'Mount Elbrus', 1874)")
    cur.execute("INSERT INTO summits VALUES('Jacques Balmat', 'Mount Blanc', 1786)")
    cur.execute("INSERT INTO summits VALUES('Michel Paccard', 'Mount Blanc', 1786)")
    con.commit()

    'joining tables: mountains and summits'
    'http://stackoverflow.com/questions/2945594/python-sqlite3-wont-execute-a-join-but-sqlite3-alone-will'
    combined = cur.execute("SELECT Mountains.Mountain, Continent, Height, Person, Year FROM Summits INNER JOIN Mountains on Mountains.Mountain = Summits.Mountain")   
    
    'WHY AM I ONLY PRINTING 8 ROWS?'
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    combined = pd.DataFrame(rows, columns=cols)
    
    'Print Statement'
    mount_everest = pd.read_sql("SELECT Person from Summits where Mountain='Mount Everest'",con)    
    
    print combined
    print '\n' + "The first person(s) to climb mount everest is %s." % (mount_everest)
    
    
    
    
    
    
    
    
    
    
    
    