# 13. Genera un Dataframe que tenga la estructura de la imagen y guárdalo como CSV y TSV en tu ordenador.

import psycopg2
from prettytable import PrettyTable
from time import time
from execution_time import execution_time
import pandas as pd

# Establecemos la conexión con la base de datos de PostgreSQL
conn = psycopg2.connect(
    host="localhost",       
    database="CommercialDB",  
    user="postgres",          
    password="Rs16092023"   
)

cursor = conn.cursor()

start_time = time()

ETL = """SELECT
	p.product_id AS ID_PRODUCTO,
	p.product_name AS NOMBRE_PRODUCTO,
	s.order_id AS ID_PEDIDO,
	s.date AS FECHA,
	CONCAT (sll.seller_id, '_', seller_name) AS VENDEDOR,
	sll.daily_target AS OBJETIVO_DIARIO,
	ROUND ((s.num_pieces_sold / sll.daily_target * 100),2) AS OBJETIVO_VENTA,
	CASE WHEN (s.num_pieces_sold * p.price) > AVG (s.num_pieces_sold * p.price) OVER () THEN 'Y' ELSE 'N' END AS VENTA_DESTACADA
FROM products p JOIN sales s ON s.product_id = p.product_id
JOIN sellers sll ON s.seller_id = sll.seller_id
GROUP BY p.product_id, p.product_name, s.order_id, s.date, sll.seller_id, sll.daily_target, p.price"""
cursor.execute(ETL)
rows = cursor.fetchall()

# Crear tabla para mostrar los resultados
tabla_ETL = PrettyTable()
tabla_ETL.field_names = [desc[0] for desc in cursor.description]
tabla_ETL.add_rows(rows)

print(tabla_ETL)

columns = [desc[0] for desc in cursor.description]
result_df = pd.DataFrame(rows, columns=columns)

# Ruta donde se guardará el archivo CSV
ruta_guardado = 'C:\\Users\\rauls\\OneDrive\\Escritorio'

# Guardar el DataFrame en un archivo CSV
ruta_csv = ruta_guardado + '\\Df_csv.csv'
result_df.to_csv(ruta_csv, index=False)

ruta_tsv = ruta_guardado + '\\Df_tsv.tsv'
result_df.to_csv(ruta_tsv, index=False, sep = "\t")

print(f"El resultado se ha guardado en {ruta_csv}")

end_time = time()

execution_time(start_time, end_time)

cursor.close()
conn.close()
