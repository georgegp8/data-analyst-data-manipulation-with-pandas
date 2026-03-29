# ================================================
# Ejercicios Estadísticas Resumidas Agrupadas 
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the sales dataset
sales = pd.read_csv('../sales_subset.csv')

# ------------------------------------------------
# Sección 1: ¿Qué porcentaje de ventas se produjo en cada tipo de tienda?
# ------------------------------------------------
# Aunque .groupby() es útil, puedes calcular estadísticas sumarias agrupadas sin él.
#
# Walmart distingue tres tipos de tiendas: "supercentros", "tiendas de descuento" y "mercados de barrio".
# Codificados en este conjunto de datos como tipo "A", "B" y "C". En este ejercicio, calcularás las ventas totales
# realizadas en cada tipo de tienda, sin utilizar .groupby(). A continuación, puedes utilizar estas cifras para
# ver qué proporción de las ventas totales de Walmart se realizaron en cada tipo.
#
# sales está disponible y pandas se importa como pd.

# Instrucciones:
# - Calcula el total de weekly_sales en todo el conjunto de datos.
# - Subconjunto para las tiendas type "A", y calcula sus ventas semanales totales.
# - Haz lo mismo en las tiendas type "B" y type "C".
# - Combina los resultados A/B/C en una lista y divida por sales_all para obtener la proporción de ventas
#   por tipo.

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all

# Print the result
print(sales_propn_by_type)
