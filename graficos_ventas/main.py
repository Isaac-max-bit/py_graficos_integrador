import pandas as pd

# Cargar archivo Excel
df = pd.read_excel("Productos.cvs.xlsx", engine="openpyxl")

# Mostrar las primeras filas
print(df.head())
