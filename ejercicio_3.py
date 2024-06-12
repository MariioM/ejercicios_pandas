"""
Escribir una función que reciba un diccionario con las notas de los alumnos de un curso 
y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.
"""

import pandas as pd

def aprobados(resultados):
    notas = pd.Series(resultados)
    return notas[notas >=5].sort_values(ascending=False)

boletin = {"Mario": 9, "Lucas": 4, "Pedro": 5, "Asier": 8, "Enzo": 3}
print(aprobados(boletin))