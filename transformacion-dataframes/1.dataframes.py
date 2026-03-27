# ================================================
# Ejercicios DataFrames - Part 1
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the homelessness dataset
homelessness = pd.read_csv('homelessness.csv')

# ------------------------------------------------
# Sección 1: Inspeccionar un DataFrame
# ------------------------------------------------
# Cuando se recibe un nuevo DataFrame para trabajar, lo primero que se debe hacer es explorar sus datos.
# Hay varios métodos útiles que puedes usar para observar rápidamente el DataFrame:
# - .head() devuelve las primeras filas (por defecto 5)
# - .info() muestra información sobre las columnas, tales como el tipo de datos y los valores faltantes
# - .shape devuelve el número de filas y columnas del DataFrame
# - .describe() calcula algunas estadísticas resumidas para las columnas numéricas
#
# homelessness es un DataFrame que contiene estimaciones del número de personas sin hogar en cada estado de EE.UU.
# en 2018. El índice individual es el número de fila por el cual se conoce cada fila.

# Instrucciones:
# - Imprime las primeras filas del DataFrame homelessness.
# - Imprime información sobre los tipos de datos y valores faltantes de las columnas en homelessness.
# - Imprime el número de filas y columnas en homelessness.
# - Imprime algunas estadísticas resumidas que describen las columnas numéricas de homelessness.

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

# ------------------------------------------------
# Sección 2: Partes de un DataFrame
# ------------------------------------------------
# Para comprender mejor los objetos DataFrame, es útil saber que constan de tres componentes, 
# almacenados como atributos:
# - .values: una matriz NumPy bidimensional de valores.
# - .columns: un índice de columnas, con los nombres de las columnas.
# - .index: un índice de las filas, con los números o nombres de fila.
#
# Resulta habitual pensar en los índices como una lista de cadenas o números, aunque el tipo 
# de datos Index de pandas permite opciones más sofisticadas.

# Instrucciones:
# - Importa pandas utilizando el alias pd.
# - Imprime una matriz NumPy 2D con los valores de homelessness.
# - Imprime los nombres de las columnas de homelessness.
# - Imprime el índice de homelessness.

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)