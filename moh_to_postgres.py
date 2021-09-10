# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:42:08 2021

@author: Nelly
"""

import pandas as pd
import openpyxl
from sqlalchemy import create_engine
#%%
def push(query, user= 'student_carina@academy-summer21', password = 'carina',
            host="academy-summer21.postgres.database.azure.com", port = "5432", database = 'runecaensis'):
    try:
        import psycopg2 as psy
        connection = psy.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database,
            )
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()
        cursor.close()
query = '''CREATE TABLE MOH_table(
        datakilde TEXT,
        terreng TEXT,
        x REAL,
        y REAL,
        z REAL
        )'''
push(query)




## inserting 
def inserting():
    import csv
    import psycopg2
    try: 
        conn = psycopg2.connect(user= 'student_carina@academy-summer21', password = 'carina', 
                host='academy-summer21.postgres.database.azure.com', port = "5432", database = 'runecaensis')
        cur = conn.cursor()
        with open('moh_final.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip the header row.
            for row in reader:
                cur.execute(
                "INSERT INTO MOH_table VALUES (%s, %s, %s, %s, %s)",
                row
            )
            #conn.commit()
    except: 
        "000"
    

    finally:
        conn.close()
        cur.close()

inserting()




