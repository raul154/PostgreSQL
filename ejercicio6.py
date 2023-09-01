# 6. ¿Cuántos productos distintos se han vendido cada día? Ordena el Dataframe por fecha.

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

ventaProductosDistintosDiarios = """SELECT date, total_sales 
FROM (
	SELECT DISTINCT s.date, COUNT (s.product_id) AS total_sales
	FROM sales s
	GROUP BY s.date
) subquery
ORDER BY date ASC;"""

cursor.execute(ventaProductosDistintosDiarios)
sales_rows = cursor.fetchall()

sales_table = PrettyTable()
sales_table.field_names = [desc[0] for desc in cursor.description]
sales_table.add_rows(sales_rows)

print(sales_table)

end_time = time()

execution_time (start_time, end_time)

cursor.close()
conn.close()
