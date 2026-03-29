# ================================================
# Ejercicios Contando
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the sales dataset
sales = pd.read_csv('../sales_subset.csv')

# ------------------------------------------------
# Sección 1: Eliminar duplicados
# ------------------------------------------------
# Eliminar duplicados es una habilidad esencial para obtener recuentos precisos, porque a menudo no quieres
# contar lo mismo varias veces. En este ejercicio, crearás algunos DataFrames nuevos utilizando valores únicos
# de sales.
#
# sales está disponible y pandas se importa como pd.

# Instrucciones:
# - Elimina las filas de sales con pares duplicados de store y type y guárdalo como store_types e imprime
#   el encabezado.
# - Elimina las filas de sales con pares duplicados de store y department y guárdalo como store_depts e
#   imprime el encabezado.
# - Subconjunta las filas que sean semanas de vacaciones utilizando la columna is_holiday y elimina las
#   dates duplicadas, guárdándolas como holiday_dates.
# - Selecciona la columna date de holiday_dates, e imprímela.

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])

# Print the head of store_types
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])

# Print the head of store_depts
print(store_depts.head())

# Subset the rows that are holidays and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates("date")

# Print date col of holiday_dates
print(holiday_dates["date"])
