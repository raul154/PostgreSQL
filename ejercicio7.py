# 7. ¿Cuál es el gasto medio por pedido?

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

gastoMedioPorPedido = """SELECT avg(gastoPorPedido) AS gastoMedioPorPedido
FROM (
	SELECT (s.num_pieces_sold * p.price) AS gastoPorPedido
	FROM sales s JOIN products p ON s.product_id = p.product_id
	) subquery;"""

cursor.execute(gastoMedioPorPedido)
rows = cursor.fetchall()
resultado = rows [0][0]

print(f"El gasto medio por pedido es", resultado)

end_time = time()

execution_time (start_time, end_time)

cursor.close()
conn.close()
