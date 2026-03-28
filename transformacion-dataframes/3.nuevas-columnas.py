# ================================================
# Ejercicios Nuevas Columnas - Part 1
# ================================================

# Import pandas using the alias pd
import pandas as pd

# Load the homelessness dataset
homelessness = pd.read_csv('homelessness.csv')

# ------------------------------------------------
# Sección 1: Añadir nuevas columnas
# ------------------------------------------------
# No siempre tendrás exactamente los datos de columnas correctos para tu análisis.
# A menudo querrás añadir una nueva columna que sea una combinación de columnas existentes.
# Añadir una nueva columna a un DataFrame se denomina transformación, mutación e ingeniería
# de características.
#
# Puedes crear nuevas columnas utilizando aritmética. El código de la derecha crea una nueva
# columna total, que es la suma de las columnas individuals y family_members.

# Instrucciones:
# - Añade una nueva columna a homelessness, llamada total, que contenga la suma de las columnas
#   individuals y family_members.
# - Añade otra columna a homelessness, llamada p_individuals, que contenga la proporción de
#   personas sin hogar que son individuos en lugar de miembros de familias, es decir, individuals
#   dividido entre total.

# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]

# See the result
print(homelessness)

# ------------------------------------------------
# Sección 2: ¡Combo-ataque!
# ------------------------------------------------
# Has visto el método más común de crear nuevas columnas mediante manipulación aritmética de columnas
# existentes, y también métodos más avanzados como .apply() y .map().
#
# En este ejercicio, crearás una columna nueva y usarás varias técnicas que has aprendido para
# contar una historia de los datos.

# Instrucciones:
# - Añade una columna a homelessness, indiv_per_10k, que contenga el número de personas sin hogar
#   por cada diez mil personas en cada estado.
# - Crea un subconjunto de filas donde indiv_per_10k sea superior a 20, asignándolo a high_homelessness.
# - Ordena high_homelessness por indiv_per_10k en orden descendente, asignándolo a high_homelessness_srt.
# - Selecciona solo las columnas state e indiv_per_10k de high_homelessness_srt y guárdalo como
#   result. Mira el resultado.

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]

# Subset rows where indiv_per_10k is greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# Select only the state and indiv_per_10k columns
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)
