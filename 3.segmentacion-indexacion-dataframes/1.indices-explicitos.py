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

# ------------------------------------------------
# Sección 3: Establecer índices multinivel
# ------------------------------------------------
# Los índices también pueden estar formados por varias columnas, formando un índice multinivel
# (a veces llamado índice jerárquico). Utilizarlos tiene su contrapartida.
#
# La ventaja es que los índices multinivel facilitan la interpretación a partir de variables categóricas anidadas.
# Por ejemplo, en un ensayo clínico, puedes tener grupos de control y de tratamiento. Entonces, cada sujeto de
# prueba pertenece a uno u otro grupo, y podemos decir que un sujeto de prueba está anidado dentro del grupo
# de tratamiento. Del mismo modo, en el conjunto de datos de temperatura, la ciudad está anidada en el país, por
# lo que podemos decir que una ciudad está anidada dentro del país.
#
# El principal inconveniente es que el código para manipular índices es distinto del código para manipular
# columnas, por lo que tienes que aprender dos sintaxis y estar al tanto de cómo se representan tus datos.
#
# pandas se carga como pd. temperatures está disponible.

# Instrucciones:
# - Establece el índice de temperatures en las columnas "country" y "city", y asignado a
#   temperatures_ind.
# - Especifica dos pares país/ciudad a conservar: "Brazil" / "Rio De Janeiro" y "Pakistan" / "Lahore",
#   asignando a rows_to_keep.
# - Imprime y subconjunta temperatures_ind para rows_to_keep utilizando .loc[].

# Index temperatures by country and city
temperatures_ind = temperatures.set_index(["country", "city"])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [("Brazil", "Rio De Janeiro"), ("Pakistan", "Lahore")]

# Subset for rows in rows_to_keep
print(temperatures_ind.loc[rows_to_keep])

# ------------------------------------------------
# Sección 4: Ordenar por valores índice
# ------------------------------------------------
# Antes, cambiabas el orden de las filas de un DataFrame llamando a .sort_values(). También es útil poder
# ordenar por elementos del índice. Para ello, tienes que utilizar .sort_index().
#
# pandas se carga como pd. temperatures_ind tiene un índice multinivel de country y city, y está disponible.

# Instrucciones:
# - Ordena temperatures_ind por los valores del índice.
# - Ordena temperatures_ind por los valores del índice en el nivel "city".
# - Ordena temperatures_ind por país ascendente y ciudad descendente.

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True, False]))



