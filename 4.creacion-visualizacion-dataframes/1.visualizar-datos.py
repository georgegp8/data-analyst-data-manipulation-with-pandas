# ================================================
# Ejercicio: Visualizar Datos
# ================================================

# Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Load the avocados dataset
avocados = pd.read_pickle('../avoplotto.pkl')

# ------------------------------------------------
# Sección 1: ¿Qué tamaño de aguacate es el más popular?
# ------------------------------------------------
# Los aguacates son cada vez más populares y están deliciosos ya sea en forma de guacamole o sobre una
# tostada. El Hass Avocado Board lleva un programa de seguimiento de la oferta y la demanda de aguacates
# en todo Estados Unidos, incluidas las ventas de tres tamaños diferentes de aguacates. En este ejercicio,
# utilizarás un diagrama de barras para averiguar qué tamaño es el más popular.
#
# Los gráficos de barras son estupendos para revelar las relaciones entre variables categóricas (tamaño) y
# numéricas (número vendido), pero a menudo tendrás que manipular primero los datos para obtener los
# números que necesitas para el gráfico.
#
# pandas se ha importado como pd y avocados está disponible.

# Instrucciones:
# - Imprime el encabezado del conjunto de datos avocados. ¿Qué columnas están disponibles?
# - Para cada grupo de tamaño de aguacate, calcula el número total vendido, almacenándolo como
#   nb_sold_by_size.
# - Crea un diagrama de barras del número de aguacates vendidos por tamaño.
# - Muestra el gráfico.

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")

# Show the plot
plt.show()
