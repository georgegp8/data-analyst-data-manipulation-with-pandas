# ================================================
# Ejercicio: CSV a DataFrame
# ================================================

# Import pandas
import pandas as pd

# ------------------------------------------------
# Sección 1: Leer CSV como DataFrame
# ------------------------------------------------
# Trabajas para una compañía aérea y tu jefe te ha pedido que hagas un análisis de la competencia y veas
# con qué frecuencia los pasajeros que vuelan en otras compañías son expulsados involuntariamente de sus
# vuelos. Has obtenido un archivo CSV (airline_bumping.csv) del Departamento de Transporte con datos
# sobre los pasajeros a los que se les denegó el embarque de forma involuntaria en 2016 y 2017, pero no
# contiene las cifras exactas que necesitas. Para averiguarlo, tendrás que importar el CSV a un DataFrame de
# pandas y realizar algunas manipulaciones.
#
# Se ha importado pandas como pd. "airline_bumping.csv" está en tu directorio de trabajo.

# Instrucciones 1/4:
# - Lee el archivo CSV "airline_bumping.csv" y guárdalo como un DataFrame llamado airline_bumping.
# - Imprime las primeras filas de airline_bumping.

# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("airline_bumping.csv")

# Take a look at the DataFrame
print(airline_bumping.head())

# Instrucciones 2/4:
# - Para cada grupo de aerolíneas, selecciona las columns nb_bumped y total_passengers, y calcula la
#   suma (para ambos años). Guárdalo como airline_totals.

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()

# Instrucciones 3/4:
# - Crea una nueva columna de airline_totals llamada bumps_per_10k, que es el número de pasajeros
#   accidentados por cada 10,000 pasajeros para cada aerolínea.

# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Instrucciones 4/4:
# - Imprime airline_totals para ver los resultados de tus manipulaciones.

# Print airline_totals
print(airline_totals)
