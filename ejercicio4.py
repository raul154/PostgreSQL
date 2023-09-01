# 4. ¿Cuántos productos se han vendido al menos una vez?

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

totalProductosVendidos = """SELECT COUNT(*) AS total_productos_vendidos
FROM products
WHERE product_id IN (
    SELECT DISTINCT product_id
    FROM sales
);"""

cursor.execute(totalProductosVendidos)
products_rows = cursor.fetchall()
total_productos_vendidos = products_rows[0][0]

end_time = time()

execution_time (start_time, end_time)

print (f"El número de productos vendidos al menos una vez es:", total_productos_vendidos)

cursor.close()
conn.close()
