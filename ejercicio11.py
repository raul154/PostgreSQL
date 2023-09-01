# 11.	Calcula el total vendido por cada vendedor y muéstralo, ordenando de mayor a menor total vendido.

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

cantidadEuros = """SELECT seller_id, SUM(gastoPorProducto) AS dineroGenerado
FROM (
  SELECT s.seller_id, (s.num_pieces_sold * p.price) AS gastoPorProducto
  FROM sales s
  JOIN products p ON s.product_id = p.product_id
) AS subquery
GROUP BY seller_id
ORDER BY dineroGenerado DESC;"""

cursor.execute(cantidadEuros)
rows = cursor.fetchall()

# Crear tabla para mostrar los resultados
tabla_euros = PrettyTable()
tabla_euros.field_names = [desc[0] for desc in cursor.description]
tabla_euros.add_rows(rows)

print(tabla_euros)

end_time = time()

execution_time (start_time, end_time)

cursor.close()
conn.close()
