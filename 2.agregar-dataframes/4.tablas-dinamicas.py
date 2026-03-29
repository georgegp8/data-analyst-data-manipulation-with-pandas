# ================================================
# Ejercicios Tablas Dinámicas - Part 1
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the sales dataset
sales = pd.read_csv('../sales_subset.csv')

# ------------------------------------------------
# Sección 1: Dinamizar sobre una variable
# ------------------------------------------------
# Las tablas dinámicas son la forma estándar de agregar datos en las hojas de cálculo.
#
# En pandas, las tablas dinámicas son esencialmente otra forma de realizar cálculos agrupados. Es decir, el
# método .pivot_table() es una alternativa a .groupby().
#
# En este ejercicio, realizarás cálculos utilizando .pivot_table() para reproducir los cálculos que realizaste
# en la lección anterior utilizando .groupby().
#
# sales está disponible y pandas se importa como pd.

# Instrucciones:
# - Obtén la media de weekly_sales mediante type utilizando .pivot_table() y almacénala como
#   mean_sales_by_type.
# - Obtener la media y la mediana de weekly_sales por type utilizando .pivot_table() y almacenarlas como
#   mean_med_sales_by_type.
# - Obtén la media de weekly_sales mediante type e is_holiday mediante .pivot_table() y guárdalo como
#   mean_sales_by_type_holiday.

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Pivot for mean and median weekly_sales by each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=["mean", "median"])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# ------------------------------------------------
# Sección 2: Rellenar los valores que faltan y sumar valores con tablas dinámicas
# ------------------------------------------------
# El método .pivot_table() tiene varios argumentos útiles, como fill_value y margins.
#
# - fill_value sustituye los valores que faltan por un valor real (lo que se conoce como imputación). Con
#   qué sustituir los valores aumenta es un tema lo suficientemente amplio como para tener su propio curso
#   (Cómo tratar los datos ausentes en Python), pero lo más sencillo es sustituirlos por un valor ficticio.
#
# - margins es un atajo para cuando dinamizas por dos variables, pero también quieres dinamizar por cada
#   una de esas variables por separado: da los totales de fila y columna del contenido de la tabla dinámica.
#
# En este ejercicio, practicarás el uso de estos argumentos para mejorar tus habilidades con las tablas
# dinámicas, ¡lo que te ayudará a hacer números de forma más eficiente!
#
# sales está disponible y pandas se importa como pd.

# Instrucciones:
# - Imprime la media weekly_sales por department y type completando los valores que faltan con 0.
# - Imprime la media weekly_sales por department y type completando los valores que faltan con 0 y sumando
#   todas las filas y columnas.

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index="type", columns="department", fill_value=0))

# Print mean weekly_sales by department and type; fill missing values with 0; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))

