# ================================================
# Ejercicio: Valores Ausentes
# ================================================

# Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Load the avocados dataset
avocados = pd.read_pickle('../avoplotto.pkl')
# Subset for 2016 data
avocados_2016 = avocados[avocados["year"] == 2016]

# ------------------------------------------------
# Sección 1: Encontrar valores ausentes
# ------------------------------------------------
# Los valores ausentes están por todas partes y no quieres que interfieran en tu trabajo. Algunas funciones
# ignoran por defecto los datos que faltan, pero no siempre es ése el comportamiento que puedes desear.
# Algunas funciones no pueden manejar valores omitidos en absoluto, por lo que hay que ocuparse de estos
# valores antes de poder utilizarlas. Si no sabes dónde están tus valores ausentes, o si existen, podrías cometer
# errores en tu análisis. En este ejercicio, determinarás si faltan valores en el conjunto de datos y, en caso
# afirmativo, cuántos.
#
# pandas se ha importado como pd y avocados_2016, un subconjunto de avocados que solo contiene las
# ventas de 2016.

# Instrucciones:
# - Imprime un DataFrame que muestre si falta o no cada valor de avocados_2016.
# - Imprime un resumen que muestre si falta algún valor o no en cada columna.
# - Crea un diagrama de barras del número total de valores ausentes en cada columna.

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")

# Show plot
plt.show()

# ------------------------------------------------
# Sección 2: Eliminar valores ausentes
# ------------------------------------------------
# Ahora que sabes que hay algunos valores ausentes en tu DataFrame, tienes algunas opciones para tratarlos.
# Una forma es eliminarlos completamente del conjunto de datos. En este ejercicio, eliminarás los valores
# ausentes eliminando todas las filas que contengan valores ausentes.
#
# pandas se ha importado como pd y avocados_2016 está disponible.

# Instrucciones:
# - Elimina las filas de avocados_2016 que contengan valores ausentes y almacena las filas restantes en
#   avocados_complete.
# - Comprueba que se han eliminado todos los valores que faltan de avocados_complete. Calcula cada
#   columna que tenga NA e imprímela.

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())

# ------------------------------------------------
# Sección 3: Sustitución de valores ausentes
# ------------------------------------------------
# Otra forma de tratar los valores que faltan es sustituirlos todos por el mismo valor. Para las variables
# numéricas, una opción es sustituir los valores por 0- lo harás aquí. Sin embargo, cuando sustituyes valores
# ausentes, haces suposiciones sobre lo que significa un valor ausente. En este caso, supondrás que la falta de
# un número vendido significa que no se realizaron ventas de ese tipo de aguacate esa semana.
#
# En este ejercicio, verás cómo la sustitución de valores ausentes puede afectar a la distribución de una
# variable utilizando histogramas. Puedes trazar histogramas de varias variables a la vez de la siguiente forma:
#
# dogs[["height_cm", "weight_kg"]].hist()
#
# pandas se ha importado como pd y matplotlib.pyplot se ha importado como plt. El conjunto de datos
# avocados_2016 está disponible.

# Instrucciones 1/2:
# - Se ha creado una lista, cols_with_missing, que contiene los nombres de las columnas con valores
#   ausentes: "small_sold", "large_sold" y "xl_sold".
# - Crea un histograma de esas columnas.
# - Muestra el gráfico.

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

# Instrucciones 2/2:
# - Sustituye los valores que faltan de avocados_2016 por 0 y guarda el resultado como avocados_filled.
# - Crea un histograma de las columnas cols_with_missing de avocados_filled.

# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()
