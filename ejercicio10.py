# 10. Calcula el total vendido.

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

gastoTotalEnEuros = """SELECT SUM (gastoPorProducto) AS gastoTotalEnEuros
FROM (
	SELECT (s.num_pieces_sold * p.price) AS gastoPorProducto
	FROM sales s JOIN products p ON s.product_id = p.product_id
	)subquery;"""

cursor.execute(gastoTotalEnEuros)
rows = cursor.fetchall()
resultado = rows [0][0]

print (f"El gasto total en euros ha sido", resultado)

end_time = time()

execution_time (start_time, end_time)

cursor.close()
conn.close()
