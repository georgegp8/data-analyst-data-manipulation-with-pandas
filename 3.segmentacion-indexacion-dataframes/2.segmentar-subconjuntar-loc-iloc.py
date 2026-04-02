# ================================================
# Ejercicio: Segmentar y subconjuntar con .loc[] e .iloc[]
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the temperatures dataset
temperatures = pd.read_csv('../temperatures.csv')
temperatures_ind = temperatures.set_index(["country", "city"])

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

# ------------------------------------------------
# Sección 2: Segmentar en ambas direcciones
# ------------------------------------------------
# Ya has visto segmentar los DataFrames por filas o por columnas, pero como los DataFrames son objetos
# bidimensionales, a menudo es natural segmentar ambas dimensiones a la vez. Es decir, pasando dos
# argumentos a .loc[], puedes subconjuntar por filas y columnas de una sola vez.
#
# pandas se carga como pd. temperatures_srt está indexado por país y ciudad, tiene un índice ordenado y
# está disponible.

# Instrucciones:
# - Utiliza .loc[] para subdividir las filas de India, Hyderabad a Iraq, Baghdad.
# - Utiliza la segmentación .loc[] para subconjuntar columnas de date a avg_temp_c.

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad"), "date":"avg_temp_c"])

# ------------------------------------------------
# Sección 3: Cortar series temporales
# ------------------------------------------------
# La segmentación es especialmente útil para las series temporales, ya que es habitual querer filtrar los datos
# dentro de un intervalo de fechas. Añade la columna date al índice y utiliza .loc[] para realizar el
# subconjunto. Lo importante es recordar que las fechas deben estar en formato ISO 8601, es decir,
# "yyyy-mm-dd" para el año-mes-día, "yyyy-mm" para el año-mes y "yyyy" para el año.
#
# Recuerda del Capítulo 1 que puedes combinar varias condiciones booleanas utilizando operadores lógicos,
# como &. Para hacerlo en una línea de código, tendrás que añadir paréntesis () alrededor de cada
# condición.
#
# pandas se carga como pd y temperatures, sin índice, está disponible.

# Instrucciones:
# - Utiliza condiciones booleanas, no .isin() ni .loc[], y la fecha completa "yyyy-mm-dd", para
#   subconjuntar temperatures para las filas en las que la columna date esté en 2010 y 2011 e imprime los
#   resultados.
# - Establece el índice de temperatures en la columna date y ordénalo.
# - Utiliza .loc[] para subconjuntar temperatures_ind para las filas de 2010 y 2011.
# - Utiliza .loc[] para subconjuntar temperatures_ind para las filas de August 2010 a February 2011.

# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

# Set date as the index and sort the index
temperatures_ind_date = temperatures.set_index(["date"]).sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind_date.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind_date.loc["2010-08":"2011-02"])

# ------------------------------------------------
# Sección 4: Subconjunto por número de fila/columna
# ------------------------------------------------
# Las formas más habituales de subconjuntar filas son las que hemos comentado anteriormente: mediante una
# condición booleana o por etiquetas de índice. Sin embargo, a veces también es útil pasar números de fila.
#
# Esto se hace utilizando .iloc[], y, al igual que .loc[], puede tomar dos argumentos para permitirte hacer
# subconjuntos por filas y columnas.
#
# pandas se carga como pd. temperatures (sin índice) está disponible.

# Instrucciones:
# - Utiliza .iloc[] en temperatures para tomar subconjuntos.
# - Obtén la fila 23, columna 2 (posiciones índice 22 y 1).
# - Obtén las 5 primeras filas (posiciones de índice 0 a 5).
# - Obtén todas las filas, columnas 3 y 4 (posiciones de índice 2 a 4).
# - Obtén las 5 primeras filas, columnas 3 y 4.

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22,1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5,2:4])
print(temperatures.head())

