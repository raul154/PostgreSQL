import pandas as pd

# Cargar el archivo CSV original
archivo_csv = 'c:\\Users\\rauls\\OneDrive\\Escritorio\\fichero_hdfs\\sales_extended_8GB.csv'
df_original = pd.read_csv(archivo_csv)

# Copiamos el contenido
df_copia = df_original.copy()

# Concatenamos el DataFrame original y la copia
df_concatenado = pd.concat([df_original, df_copia], ignore_index=True)

# Guardamos el DataFrame concatenado en el mismo archivo CSV
df_concatenado.to_csv("C:\\Users\\rauls\\OneDrive\\Escritorio\\fichero_hdfs\\sales_extended_16GB.csv", index=False)