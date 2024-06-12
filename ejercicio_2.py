"""
Escribir una función que reciba un diccionario con las notas de los alumno de un curso y devuelva una serie con 
la nota mínima, la máxima, media y la desviación típica.
"""

import pandas as pd

def serialize(dictionary):
    notas = pd.Series(dictionary)
    estadisticas = pd.Series([notas.max(), notas.min(), notas.mean() ,notas.std()], index=["Min", "Max", "Media" ,"Desvicación Típica"])
    return estadisticas

boletin = {"Mario": 9, "Lucas": 7, "Pedro": 5}

print(serialize(boletin))
