# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 08:52:01 2021

@author: Carin
"""
import pandas as pd
import openpyxl
from sqlalchemy import create_engine
        
#%%
def push(query, user= 'student_carina@academy-summer21', password = 'carina', 
            host="academy-summer21.postgres.database.azure.com", port = "5432", database = 'student_carina'):    
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

query = '''CREATE TABLE plant_table(
        Id TEXT,
        Taksonsorteringsrekkefølge TEXT,
        Valideringsstatus TEXT,
        Rødlistekategori CHAR(2),
        Artsnavn TEXT,
        Vitenskapelignavn TEXT,
        Autor TEXT,
        Skjermetfunn TEXT,
        Antall TEXT,
        Enhet TEXT,
        Alder TEXT,
        Kjønn TEXT,
        Aktivitet TEXT,
        Metode TEXT,
        Superlokalitet TEXT,
        Lokalitetsnavn TEXT,
        Østkoordinat TEXT,
        Nordkoordinat TEXT,
        Nøyaktighet TEXT,
        Originalekoordinater TEXT,
        Fylke TEXT,
        Kommune TEXT,
        Fylke1 TEXT,
        IKKEINORGE TEXT,
        Eksternid TEXT,
        Startdato TEXT,
        Stattidspunkt TEXT,
        Sluttdato TEXT,
        Sluttidspunkt TEXT,
        Kommentar TEXT,
        Ikkegjenfunnet TEXT,
        Usikkerartsbestemmelse TEXT,
        Uspontan TEXT,
        Biotop TEXT,
        Biotopbeskrivelse TEXT,
        Substrat TEXT,
        Vitenskapeligsubstratnavn TEXT,
        Artsomsubstatbeskrivelse TEXT,
        Substrat1 TEXT,
        Substratbeskrivelse TEXT,
        Mindybde TEXT,
        Maksdybde TEXT,
        Høydemin TEXT,
        Høydemaks TEXT,
        Offentligsamling TEXT,
        Privatsamling TEXT,
        Samlingsnummer TEXT,
        Samlingsbeskrivelse TEXT,
        Artsbestemtav TEXT,
        Bestemmelsesdato TEXT,
        Bekrefter TEXT,
        Bekreftelsesdato TEXT,
        Redigeringsansvarlig TEXT,
        Rapportør TEXT,
        Observatører TEXT,
        Prosjekt TEXT
        )'''

push(query)


#%%        
# Define function using cursor.executemany() to insert the dataframe
def execute_many(datafrm, table):
    
    # Creating a list of tupples from the dataframe values
    tpls = [tuple(x) for x in datafrm.to_numpy()]
    
    # dataframe columns with Comma-separated
    cols = ','.join(list(datafrm.columns))
    
    # SQL query to execute
    sql = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)" % (table, cols)
    try:
        import psycopg2 as psy
        connection = psy.connect(
                user='student_carina@academy-summer21',
                password='carina',
                host="academy-summer21.postgres.database.azure.com",
                port="5432",
                database='student_carina',
            )
      
        cursor = connection.cursor()       
        cursor.executemany(sql, tpls)
        connection.commit()
        
        print("Data inserted using execute_many() successfully...")
        
    finally:
        connection.close()
        cursor.close()

#%%
for i in range(1,  56):
    path = (f'C:/Users/Carin/OneDrive/Documents/AW academy/graduation/ExcelExport_5361632_Page_{i}.xlsx')
    file= pd.read_excel(path, header=2) 
    file.columns = file.columns.str.replace(' ', '')
    file.columns = file.columns.str.replace('.', '')
    file.columns = file.columns.str.replace(',', '')
    file.fillna(0, inplace=True)           
    execute_many(file, 'plant_table')
    
#%%
# missinglist = [46, 529]
#missinglist.append(737, 724)
for i in range(1099,  1300):
    path = (f'C:/Users/Carin/OneDrive/Documents/AW academy/graduation/ExcelExport_5362317_Page_{i}.xlsx')
    try:
        file= pd.read_excel(path, header=2) 
        file.columns = file.columns.str.replace(' ', '')
        file.columns = file.columns.str.replace('.', '')
        file.columns = file.columns.str.replace(',', '')
        file.fillna(0, inplace=True)           
        execute_many(file, 'plant_table')   
        print(i)
    except FileNotFoundError: 
        print(f"Page {i} does not exist")
        missinglist.append(i)
        continue
    
    