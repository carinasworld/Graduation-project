import pandas as pd
from psycopg2.extras import execute_batch

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
    
    conn = psycopg2.connect(user= 'student_carina@academy-summer21', password = 'carina', 
            host='academy-summer21.postgres.database.azure.com', port = "5432", database = 'runecaensis')
    cur = conn.cursor()
    with open(r'moh\moh_fullstendig_uten_nan.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        execute_batch(cur, "INSERT INTO MOH_table VALUES (%s, %s, %s, %s, %s)", [r for r in reader], page_size=1000)
        conn.commit()

inserting()


