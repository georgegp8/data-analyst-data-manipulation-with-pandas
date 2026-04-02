# ================================================
# Ejercicio: Segmentar y subconjuntar con .loc[] e .iloc[]
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the temperatures dataset
temperatures_ind = pd.read_csv('../temperatures.csv').set_index(["country", "city"])

# ------------------------------------------------
# Sección 1: Valores del índice de segmentación
# ------------------------------------------------
# Segmentar te permite seleccionar elementos consecutivos de un objeto utilizando la sintaxis first:last. Los
# DataFrames se pueden segmentar por valores índice o por número de fila/columna; empezaremos por el
# primer caso. Esto implica cortar dentro del método .loc[].
#
# En comparación con las listas de segmentación, hay algunas cosas que debes recordar.
#
# - Solo puedes segmentar un índice si está ordenado (mediante .sort_index()).
# - Para segmentar en el nivel exterior, first y last pueden ser cadenas.
# - Para segmentar en niveles internos, first y last deben ser tuplas.
# - Si pasas un único corte a .loc[], segmentará las filas.
#
# pandas se carga como pd. temperatures_ind tiene país y ciudad en el índice, y está disponible.

# Instrucciones:
# - Ordena el índice de temperatures_ind.
# - Utiliza la segmentación con .loc[] para obtener estos subconjuntos:
#   * de Pakistan a Philippines.
#   * de Lahore a Manila. (Esto devolverá un sinsentido.)
#   * de Pakistan, Lahore a Philippines, Manila.

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()
# Subset rows from Pakistan to Philippines
print(temperatures_srt.loc["Pakistan":"Philippines"])

# Try to subset rows from Lahore to Manila
print(temperatures_srt.loc["Lahore":"Manila"])

# Subset rows from Pakistan, Lahore to Philippines, Manila
print(temperatures_srt.loc[("Pakistan","Lahore"):("Philippines","Manila")])
