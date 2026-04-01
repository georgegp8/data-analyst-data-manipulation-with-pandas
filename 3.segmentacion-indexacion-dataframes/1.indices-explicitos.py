# ================================================
# Ejercicios Índices Explícitos
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the temperatures dataset
temperatures = pd.read_csv('../temperatures.csv')

# ------------------------------------------------
# Sección 1: Establecer y eliminar índices
# ------------------------------------------------
# pandas te permite designar columnas como índice. Esto permite un código más limpio al tomar subconjuntos
# (además de proporcionar una búsqueda más eficaz en algunas circunstancias).
#
# En este capítulo, explorarás temperatures, un DataFrame de temperaturas medidas en ciudades de todo el
# mundo. pandas se carga como pd.

# Instrucciones:
# - Observa temperatures.
# - Establece el índice de temperatures en "city", asignándolo a temperatures_ind.
# - Observa temperatures_ind. ¿En qué se diferencia de temperatures?
# - Restablece el índice de temperatures_ind manteniendo su contenido.
# - Restablece el índice de temperatures_ind eliminando su contenido.

# Look at temperatures
print(temperatures.head())

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# ------------------------------------------------
# Sección 2: Subconjunto con .loc[]
# ------------------------------------------------
# La función clave de los índices es .loc[]: un método de subconjunto que acepta valores de índice.
# Si le pasas un único argumento, tomará un subconjunto de filas.
#
# El código para el subconjunto que utiliza .loc[] puede ser más fácil de leer que el subconjunto
# estándar de corchetes, lo que puede hacer que tu código sea menos pesado de mantener.
#
# pandas se carga como pd. temperatures y temperatures_ind están disponibles; este último está
# indexado por city.

# Instrucciones:
# - Crea una lista llamada cities que contenga "London" y "Paris".
# - Utiliza el subconjunto [] para filtrar temperatures las filas en las que la columna city tome
#   un valor de la lista cities.
# - Utiliza el subconjunto .loc[] para filtrar temperatures_ind por las filas en las que la ciudad
#   está en la lista cities.

# Make a list of cities to subset on
cities = ["London", "Paris"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

