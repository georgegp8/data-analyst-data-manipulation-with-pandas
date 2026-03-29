# ================================================
# Ejercicios Síntesis Estadística - Part 1
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the sales dataset
sales = pd.read_csv('sales_subset.csv')

# ------------------------------------------------
# Sección 1: Media y mediana
# ------------------------------------------------
# Las estadísticas sumarias son exactamente lo que parecen: resumen muchos números en una sola estadística.
# Por ejemplo, la media, la mediana, el mínimo, el máximo y la desviación típica son estadísticas sumarias.
# Calcular estadísticas sumarias te permite hacerte una mejor idea de tus datos, aunque sean muchos.
#
# sales está disponible y pandas se carga como pd.

# Instrucciones:
# - Explora primero tu nuevo DataFrame imprimiendo las primeras filas del DataFrame sales.
# - Imprime información sobre las columnas en sales.
# - Imprime la media de la columna weekly_sales.
# - Imprime la mediana de la columna weekly_sales.

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales["weekly_sales"].mean())

# Print the median of weekly_sales
print(sales["weekly_sales"].median())
