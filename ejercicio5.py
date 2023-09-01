# 5. ¿Qué producto se ha vendido en más pedidos?

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

productosMasVendidos = """SELECT product_id, total_sales
FROM (
    SELECT product_id, COUNT(*) AS total_sales, 
			RANK() OVER (ORDER BY COUNT(*) DESC) AS rank_ventas
    FROM sales
    GROUP BY product_id
) subquery
WHERE rank_ventas = 1;"""

cursor.execute(productosMasVendidos)
products_rows = cursor.fetchall()

products_table = PrettyTable()
products_table.field_names = [desc[0] for desc in cursor.description]
products_table.add_rows(products_rows)

print(products_table)

end_time = time()

execution_time (start_time, end_time)

cursor.close()
conn.close()