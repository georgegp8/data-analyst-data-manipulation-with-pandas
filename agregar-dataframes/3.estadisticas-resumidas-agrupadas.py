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

# ------------------------------------------------
# Sección 2: Cálculos con .groupby()
# ------------------------------------------------
# El método .groupby() te facilita mucho la vida. En este ejercicio, realizarás los mismos cálculos que la
# última vez, excepto que utilizarás el método .groupby(). También realizarás cálculos sobre datos agrupados
# por dos variables para ver si las ventas difieren por tipo de tienda dependiendo de si es una semana festiva o
# no.
#
# sales está disponible y pandas se importa como pd.

# Instrucciones:
# - Agrupa sales por "type", toma la suma de "weekly_sales" y almacénalo como sales_by_type.
# - Calcula la proporción de ventas en cada tipo de tienda dividiendo por la suma de sales_by_type. Asigna
#   a sales_propn_by_type.
# - Agrupa sales por "type" e "is_holiday", toma la suma de weekly_sales y almacénalo como
#   sales_by_type_is_holiday.

# Group by type, sum weekly_sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sales_by_type.sum()

# Print the result
print(sales_propn_by_type)

# Group by type and is_holiday, calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()

# Print the result
print(sales_by_type_is_holiday)

# ------------------------------------------------
# Sección 3: Múltiples resúmenes agrupados
# ------------------------------------------------
# Anteriormente, en este capítulo, has visto que el método .agg() es útil para calcular múltiples estadísticas
# sobre múltiples variables. También funciona con datos agrupados. Puedes utilizar funciones integradas como
# min, max, mean y median.
#
# sales está disponible y pandas se importa como pd.

# Instrucciones:
# - Obtén el mínimo, máximo, la media y la mediana de weekly_sales para cada tipo de tienda utilizando
#   .groupby() y .agg(). Guárdalo como sales_stats.
# - Obtén el mínimo, máximo, la media y la mediana de unemployment y fuel_price_usd_per_l para cada
#   tipo de tienda. Guárdalo como unemp_fuel_stats.

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg(["min", "max", "mean", "median"])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg(["min", "max", "mean", "median"])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


