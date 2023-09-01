# 3. ¿Cuántos productos, ventas y vendedores hay en total?

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

# products
totalProducts = "SELECT COUNT(*) AS totalProducts FROM products;"
cursor.execute(totalProducts)
products_rows = cursor.fetchall()
total_products = products_rows[0][0]

# sales
totalSales = "SELECT SUM (num_pieces_sold) AS totalSales FROM sales;"
cursor.execute(totalSales)
sales_rows = cursor.fetchall()
total_sales = sales_rows[0][0]

# sellers
totalSellers = "SELECT COUNT (*) AS totalSellers FROM sellers;"
cursor.execute(totalSellers)
sellers_rows = cursor.fetchall()
total_sellers = sellers_rows[0][0]


end_time = time()

execution_time (start_time, end_time)

print(f"Total de productos: {total_products}, Total de ventas: {total_sales}, Total de vendedores: {total_sellers}")

cursor.close()
conn.close()
