# ================================================
# Ejercicios Síntesis Estadística 
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the sales dataset
sales = pd.read_csv('../sales_subset.csv')

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

# ------------------------------------------------
# Sección 2: Resumir fechas
# ------------------------------------------------
# Las estadísticas sumarias también pueden calcularse sobre columnas de fecha que tengan valores con el tipo
# de datos datetime64. Algunas estadísticas sumarias, como la media, no tienen mucho sentido en las fechas,
# pero otras son extremadamente útiles como, por ejemplo, el mínimo y el máximo, que te permiten ver qué
# intervalo de tiempo abarcan tus datos.
#
# sales está disponible y pandas se carga como pd.

# Instrucciones:
# - Imprime el máximo de la columna date.
# - Imprime el mínimo de la columna date.

# Print the maximum of the date column
print(sales["date"].max())

# Print the minimum of the date column
print(sales["date"].min())

# ------------------------------------------------
# Sección 3: Resúmenes eficaces
# ------------------------------------------------
# Aunque pandas y NumPy tienen muchas funciones, a veces puedes necesitar una función diferente para
# resumir tus datos.
#
# El método .agg() te permite aplicar tus propias funciones personalizadas a un DataFrame, así como aplicar
# funciones a más de una columna de un DataFrame a la vez, haciendo que tus agregaciones sean muy eficientes.
# Por ejemplo:
# - df['column'].agg(function)
#
# En la función personalizada para este ejercicio, "IQR" es la abreviatura de rango intercuartílico, que es
# el percentil 75 menos el percentil 25. Es una alternativa a la desviación típica que resulta útil si tus
# datos contienen valores atípicos.
#
# sales está disponible y pandas se carga como pd.

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Instrucciones:
# - Utiliza la función personalizada iqr definida junto con .agg() para imprimir el IQR de la columna
#   temperature_c de sales.
# - Actualiza la selección de columnas para utilizar la función personalizada iqr con .agg() para imprimir
#   el IQR de temperature_c, fuel_price_usd_per_l y unemployment, en ese orden.
# - Actualiza las funciones de agregación llamadas por .agg(): incluir iqr y "median" en ese orden.

# Print IQR of temperature_c
print(sales["temperature_c"].agg(iqr))

# Update to print IQR of temperature_c, fuel_price_usd_per_l, and unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr, "median"))

