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

# ------------------------------------------------
# Sección 2: Contar variables categóricas
# ------------------------------------------------
# Contar es una forma estupenda de tener una visión general de tus datos y de detectar curiosidades que de
# otro modo no notarías. En este ejercicio, contarás el número de cada tipo de tienda y el número de cada
# número de departamento utilizando los DataFrames que creaste en el ejercicio anterior.
#
# Los DataFrames store_types y store_depts que creaste en el último ejercicio están disponibles y pandas
# se importa como pd.

# Instrucciones:
# - Cuenta el número de tiendas de cada tienda type en store_types.
# - Cuenta la proporción de tiendas de cada tienda type en store_types.
# - Cuenta el número de tiendas de cada department en store_depts, ordenando los recuentos en orden
#   descendente.
# - Cuenta la proporción de tiendas de cada department en store_depts, ordenando las proporciones en
#   orden descendente.

# Count the number of stores of each type
store_counts = store_types["type"].value_counts()

# Print the store counts
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)

# Print the store proportions
print(store_props)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)

# Print the department counts
print(dept_counts_sorted)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)

# Print the department proportions
print(dept_props_sorted)

