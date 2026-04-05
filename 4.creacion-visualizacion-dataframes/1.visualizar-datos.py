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

# ------------------------------------------------
# Sección 2: Cambios en las ventas a lo largo del tiempo
# ------------------------------------------------
# Los gráficos de líneas están diseñados para visualizar la relación entre dos variables numéricas, donde cada
# valor de los datos está conectado con el siguiente. Son especialmente útiles para visualizar el cambio de un
# número o lo largo del tiempo, ya que cada punto temporal está conectado de forma natural con el punto
# temporal siguiente. En este ejercicio, visualizarás el cambio en las ventas de aguacate a lo largo de tres años.
#
# pandas se ha importado como pd y avocados está disponible.

# Instrucciones:
# - Obtén el número total de aguacates vendidos en cada fecha. El DataFrame tiene dos filas para cada
#   fecha: una para ecológico y otra para convencional. Guárdalo como nb_sold_by_date.
# - Crea un gráfico lineal del número de aguacates vendidos.
# - Muestra el gráfico.

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x="date",y="nb_sold_by_date",kind="line")

# Show the plot
plt.show()

# ------------------------------------------------
# Sección 3: Oferta y demanda de aguacate
# ------------------------------------------------
# Los gráficos de dispersión son ideales para visualizar relaciones entre variables numéricas. En este ejercicio,
# compararás el número de aguacates vendidos con el precio medio y verás si están relacionados. Si están
# relacionados, puedes utilizar un número para predecir el otro.
#
# matplotlib.pyplot se ha importado como plt, pandas se ha importado como pd y avocados está
# disponible.

# Instrucciones:
# - Crea un gráfico de dispersión con nb_sold en el eje x y avg_price en el eje y. Ponle el siguiente título:
#   "Number of avocados sold vs. average price".
# - Muestra el gráfico.

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()
