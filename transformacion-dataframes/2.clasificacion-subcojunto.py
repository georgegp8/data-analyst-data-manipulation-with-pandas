# ================================================
# Ejercicios DataFrames - Clasificación y Subconjunto
# ================================================

import pandas as pd

# Carga del dataset homelessness
homelessness = pd.read_csv('homelessness.csv')

# ------------------------------------------------
# Sección 1: Ordenar filas
# ------------------------------------------------
# Encontrar datos interesantes en un DataFrame suele ser más fácil si cambias el orden de las filas. 
# Puedes ordenar las filas pasando un nombre de columna a .sort_values().
#
# En los casos en que las filas tengan el mismo valor, puedes romper los empates ordenando sobre 
# otra columna pasando una lista de nombres de columnas.
#
# Instrucciones:
# 1. Ordena homelessness por la columna individuals, de menor a mayor, y guárdalo como homelessness_ind.
# 2. Ordena homelessness por la columna family_members en orden descendente y guárdalo como homelessness_fam.
# 3. Ordena homelessness primero por region (ascendente) y luego por family_members (descendente). 
#    Guárdalo como homelessness_reg_fam.

# --- Paso 1 ---
# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals", ascending=True)

# Print the top few rows
print(homelessness_ind.head())

# --- Paso 2 ---
# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Print the top few rows
print(homelessness_fam.head())

# --- Paso 3 ---
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())

# ------------------------------------------------
# Sección 2: Subconjunto de columnas
# ------------------------------------------------
# Cuando trabajas con datos, puede que no necesites todas las variables de tu conjunto de datos. 
# Los corchetes ( [] ) pueden utilizarse para seleccionar solo las columnas que te interesen 
# en un orden que tenga sentido para ti.
#
# Instrucciones:
# 1. Crea una Serie llamada individuals que contenga solo la columna individuals de homelessness.
# 2. Crea un DataFrame llamado state_fam que contenga solo las columnas state y family_members 
#    de homelessness, en ese orden.
# 3. Crea un DataFrame llamado ind_state que contenga las columnas individuals y state 
#    de homelessness, en ese orden.

# --- Paso 1 ---
# Select the individuals column
individuals = homelessness["individuals"]

# Print the head of the result
print(individuals.head())

# --- Paso 2 ---
# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]

# Print the head of the result
print(state_fam.head())

# --- Paso 3 ---
# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# Print the head of the result
print(ind_state.head())

# ------------------------------------------------
# Sección 3: Subconjunto de filas
# ------------------------------------------------
# Una parte de la ciencia de los datos consiste en encontrar qué partes del conjunto de datos son interesantes.
# Una de las técnicas más sencillas para ello es hallar un subconjunto de filas que coincida con algún criterio.
# A esto se le conoce como filtrado de filas o selección de filas.
#
# Existen muchas formas de crear un subconjunto de un DataFrame, quizás la más común es usar operadores relacionales
# para devolver True o False para cada fila, y luego pasar ese resultado entre corchetes.
#
# Ejemplos:
# - dogs[dogs["height_cm"] > 60]
# - dogs[dogs["color"] == "tan"]
#
# Puedes filtrar por varias condiciones a la vez utilizando el operador &.
# Ejemplo:
# - dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]
#
# homelessness está disponible y pandas se carga como pd.

# Instrucciones:
# - Filtra homelessness para los casos donde el número de individuals sea superior a diez mil,
#   asignándolos a ind_gt_10k. Muestra el resultado.
# - Filtra homelessness para los casos donde el código del censo de EE.UU. region es "Mountain",
#   asignándolos a mountain_reg. Muestra el resultado.
# - Filtra homelessness para los casos donde el número de family_members sea inferior a mil
#   y el region sea "Pacific", asignándolo a fam_lt_1k_pac. Muestra el resultado.

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]

# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]

# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)
