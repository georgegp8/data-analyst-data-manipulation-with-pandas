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
