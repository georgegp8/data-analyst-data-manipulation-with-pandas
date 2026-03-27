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