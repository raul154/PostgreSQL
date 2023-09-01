# 9. Une los tres dataframes en un solo Dataframe y muestra 10 registros en su totalidad.

# Pretty table da problemas en este ejercicio

import psycopg2
from prettytable import PrettyTable
from time import time
from execution_time import execution_time

# Establecemos la conexión con la base de datos de PostgreSQL
conn = psycopg2.connect(
    host="localhost",       
    database="CommercialDB",  
    user="postgres",          
    password="Rs16092023"   
)

cursor = conn.cursor()

start_time = time()

unionDf = """SELECT * FROM products p
JOIN sales s ON p.product_id = s.product_id 
JOIN sellers sll ON s.seller_id = sll.seller_id
ORDER BY p.product_id
LIMIT 10"""

cursor.execute(unionDf)
rows = cursor.fetchall()

print(rows)

end_time = time()

execution_time (start_time, end_time)

cursor.close()
conn.close()
