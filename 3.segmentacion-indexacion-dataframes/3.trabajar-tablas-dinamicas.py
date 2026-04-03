# ================================================
# Ejercicio: Trabajar con Tablas Dinámicas
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the temperatures dataset
temperatures = pd.read_csv('../temperatures.csv')

# ------------------------------------------------
# Sección 1: Temperatura dinámica por ciudad y año
# ------------------------------------------------
# Es interesante ver cómo cambian las temperaturas de cada ciudad a lo largo del tiempo; si se mira cada mes,
# se obtiene una gran tabla, que puede ser difícil de interpretar. En su lugar, veamos cómo cambian las
# temperaturas por año.
#
# Puedes acceder a los componentes de una fecha (año, mes y día) utilizando código de la forma
# dataframe["column"].dt.component. Por ejemplo, el componente del mes es
# dataframe["column"].dt.month, y el componente del año es dataframe["column"].dt.year.
#
# Una vez que tengas la columna del año, puedes crear una tabla dinámica con los datos agregados por
# ciudad y año, que explorarás en los próximos ejercicios.
#
# pandas se carga como pd. temperatures está disponible.

# Instrucciones:
# - Añade una columna year a temperatures, a partir del componente year de la columna date.
# - Haz una tabla dinámica de la columna avg_temp_c, con country y city como filas, y year como
#   columnas. Asigna a temp_by_country_city_vs_year y observa el resultado.

# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c",index=["country","city"],columns="year")

# See the result
print(temp_by_country_city_vs_year)
