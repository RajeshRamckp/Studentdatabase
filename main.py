import pandas as pd
import sqlite3
import pyodbc
#Enter the file name
filename="first_data.csv"
data=pd.read_csv(filename,delimiter=',')
num_cols = len(data.axes[1])
col_count = [len(l.split(",")) for l in data.columns]
conn = sqlite3.connect('stud.db')
c = conn.cursor()
#Cleaning header values
da_columns =[row.lower().replace(" ", "_").replace("-","_").replace(r"/","_").replace("\\","_").replace(".","_").replace("$","").replace("%","") for row in data.columns]

tablename="studentdetails"
#creating query to dynamically create heaader in the database

sql_query = 'CREATE TABLE studentdetails('
for name in range(0, len(col_count)):
    sql_query  += "{} varchar(100),".format(da_columns[name])
sql_query  = sql_query.rstrip(" ,")
sql_query  += ')'
cur = conn.cursor()
c.execute(sql_query)
for value in data.iterrows():
    querry_for_insert="INSERT INTO "+tablename+" ({}) VALUES ({})".format(' ,'.join(da_columns),', '.join(['?']*len(da_columns)))
    c.execute(querry_for_insert,tuple(value[1]))
conn.commit()


