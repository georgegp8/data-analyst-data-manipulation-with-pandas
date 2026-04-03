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

# ------------------------------------------------
# Sección 2: Subconjunto de tablas dinámicas
# ------------------------------------------------
# Una tabla dinámica no es más que un DataFrame con índices ordenados, por lo que las técnicas que ya has
# aprendido pueden utilizarse para subdividirlos. En particular, la combinación .loc[] + segmentar suele ser
# útil.
#
# pandas se carga como pd. temp_by_country_city_vs_year está disponible.

# Instrucciones:
# - Utiliza .loc[] en temp_by_country_city_vs_year para tomar subconjuntos.
# - Desde Egypt a India.
# - Desde Egypt, Cairo a India, Delhi.
# - Desde Egypt, Cairo a India, Delhi y de 2005 a 2010.

# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt":"India"]
# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi")]
# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi"),"2005":"2010"]

# ------------------------------------------------
# Sección 3: Calcular en una tabla dinámica
# ------------------------------------------------
# Las tablas dinámicas están llenas de estadísticas resumidas, pero solo son un primer paso para encontrar
# algo revelador. A menudo necesitarás realizar más cálculos sobre ellos. Algo habitual es encontrar las filas
# o columnas donde se produce el valor más alto o más bajo.
#
# Recuerda del Capítulo 1 que puedes subconjuntar fácilmente una Serie o un DataFrame para encontrar
# filas que cumplan una condición lógica usando una sintaxis por ejemplo: series[series > value].
#
# pandas se carga como pd y el DataFrame temp_by_country_city_vs_year está disponible. El .head()
# de este DataFrame se muestra en continuación, con solo algunas de las columnas del año mostradas:
#
# country      city         2000     2001     2002     ...    2013
# Afghanistan  Kabul        15.823   15.848   15.715   ...    16.206
# Angola       Luanda       24.410   24.427   24.791   ...    24.554
# Australia    Melbourne    14.320   14.180   14.076   ...    14.742
#              Sydney       17.567   17.854   17.734   ...    18.090
# Bangladesh   Dhaka        25.905   25.931   26.095   ...    26.587

# Instrucciones:
# - Calcula la temperatura media de cada año, asignándola a mean_temp_by_year.
# - Filtra mean_temp_by_year para el año que tuvo la temperatura media más alta.
# - Calcula la temperatura media de cada ciudad (a través de las columnas), asignándola a
#   mean_temp_by_city.
# - Filtra mean_temp_by_city para la ciudad que tuvo la temperatura media más baja.

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean(axis="index")

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])


