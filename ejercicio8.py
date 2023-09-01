# 8. Calcula el porcentaje medio que aporta un pedido a la cuota de un vendedor.

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

aportacionMediaCuota = """SELECT sll.seller_id, round(avg(cuotaPorPedido), 4) AS aportacionMediaCuota

FROM (
	SELECT sll.seller_id, (s.num_pieces_sold / sll.daily_target * 100) AS cuotaPorPedido
	FROM sales s JOIN sellers sll ON s.seller_id = sll.seller_id
	) subquery
JOIN sellers sll ON subquery.seller_id = sll.seller_id

GROUP BY sll.seller_id
ORDER BY seller_id ASC;"""

cursor.execute(aportacionMediaCuota)
rows = cursor.fetchall()

resultado = PrettyTable()
resultado.field_names = [desc[0] for desc in cursor.description]
resultado.add_rows(rows)

print(resultado)

end_time = time()

execution_time (start_time, end_time)

cursor.close()
conn.close()
