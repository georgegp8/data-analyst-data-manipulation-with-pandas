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
