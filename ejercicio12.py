# 12. Filtra este Dataframe mostrando solo las ventas hechas los días 10 de cada mes y muestralo.

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

ventasDia10 = """SELECT * FROM sales 
WHERE EXTRACT (DAY FROM date) = 10;"""
cursor.execute(ventasDia10)
rows = cursor.fetchall()

tabla_ventas = PrettyTable()
tabla_ventas.field_names = [desc[0] for desc in cursor.description]
tabla_ventas.add_rows(rows)

print(tabla_ventas)

end_time = time()

execution_time (start_time, end_time)

cursor.close()
conn.close()
