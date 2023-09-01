# 2. Muestra la totalidad de los registros de cada uno.

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
select_products = "SELECT * FROM products ORDER BY product_id ASC;"
cursor.execute(select_products)
products_rows = cursor.fetchall()

products_table = PrettyTable()
products_table.field_names = [desc[0] for desc in cursor.description]
products_table.add_rows(products_rows)

print("PRODUCTS:")
print (products_table)

# sales
select_sales = "SELECT * FROM sales ORDER BY order_id ASC;"
cursor.execute(select_sales)
sales_rows = cursor.fetchall()

sales_table = PrettyTable()
sales_table.field_names = [desc[0] for desc in cursor.description]
sales_table.add_rows(sales_rows)

print("\nSALES:")
print (sales_table)

# sellers
select_sellers = "SELECT * FROM sellers ORDER BY seller_id ASC;"
cursor.execute(select_sellers)
sellers_rows = cursor.fetchall()

sellers_table = PrettyTable()
sellers_table.field_names = [desc[0] for desc in cursor.description]
sellers_table.add_rows(sellers_rows)

print("\nSELLERS:")
print (sellers_table)

end_time = time()

execution_time (start_time, end_time)

cursor.close()
conn.close()