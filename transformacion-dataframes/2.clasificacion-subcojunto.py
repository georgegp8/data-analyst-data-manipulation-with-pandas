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