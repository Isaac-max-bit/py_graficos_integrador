import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar archivo Excel
df = pd.read_excel("C:/Users/CESDE/Desktop/graficos_ventas/Productos.cvs.xlsx", engine="openpyxl")

# Mostrar las columnas disponibles (opcional)
print("Columnas disponibles:", df.columns)

# Ajustes generales de estilo
sns.set(style="whitegrid")

# Gráfico de barras por categoría con etiquetas
if 'Categoría' in df.columns:
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(data=df, x='Categoría', width=0.5)

    # Agregar los números arriba de cada barra
    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width() / 2.,  # posición X centrada
            height + 0.5,                    # un poco arriba de la barra
            int(height),                     # el número como entero
            ha="center"
        )

    plt.title('Cantidad de productos por categoría')
    plt.xticks(rotation=10)
    plt.tight_layout()
    plt.show()
else:
    print("No se encontró la columna 'Categoría'")

# Gráfico de dispersión con puntos más pequeños
if 'Precio' in df.columns and 'Cantidad' in df.columns:
    plt.figure(figsize=(4, 3))
    sns.scatterplot(data=df, x='Precio', y='Cantidad', s=30)
    plt.title('Relación entre precio y cantidad')
    plt.tight_layout()
    plt.show()
else:
    print("No se encontraron las columnas 'Precio' y/o 'Cantidad'")
