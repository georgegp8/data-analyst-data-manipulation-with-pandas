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

# ------------------------------------------------
# Sección 4: Estadísticas acumulativas
# ------------------------------------------------
# Las estadísticas acumuladas o acumulativas también pueden ser útiles para hacer un seguimiento de las
# estadísticas resumidas a lo largo del tiempo. En este ejercicio, calcularás la suma acumulada y el máximo
# acumulado de las ventas semanales de un departamento, lo que te permitirá identificar cuáles han sido los
# meses con las ventas totales más altas hasta el momento.
#
# Se te ha creado un DataFrame llamado sales_1_1, que contiene los datos de ventas del departamento 1 de
# la tienda 1. pandas se carga como pd.

# Instrucciones:
# - Ordena las filas de sales_1_1 por la columna date en orden ascendente.
# - Obtén la suma acumulada de weekly_sales y añádelo como una nueva columna de sales_1_1 llamada
#   cum_weekly_sales.
# - Obtén el máximo acumulado de weekly_sales, y añádelo como una columna llamada cum_max_sales.
# - Imprime las columnas date, weekly_sales, cum_weekly_sales y cum_max_sales.

# Create sales_1_1 with data for store 1, type 1
sales_1_1 = sales[(sales["store"] == 1) & (sales["type"] == "A")]

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date", ascending=True)

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])


