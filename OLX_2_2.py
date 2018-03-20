import pandas as pd
import mysql.connector

cnx = mysql.connector.connect(user='candidate', database='main', password='Jy3AAmXk14', host='155.130.2.3')
query = """
SELECT *
FROM Table
"""
data = pd.read_sql(query, cnx)
cnx.close()

data.to_csv('OLX_sql_data.csv', index=False, sep=";")



