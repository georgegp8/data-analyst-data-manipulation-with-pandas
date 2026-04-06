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
