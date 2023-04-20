import csv
from collections import Counter


#
def media(lista):
    sumar = list(map(lambda x: round(float(x), 2), lista))
    imprimir("Media", sum(sumar) / len(lista))


def imprimir(texto, valor):
    print('{} {}'.format(texto, valor))


def moda(datos):
    repeticiones = 0
    for i in datos:
        n = datos.count(i)
        if n > repeticiones:
            repeticiones = n
    moda = []
    for i in datos:
        n = datos.count(i)
        if n == repeticiones and i not in moda:
            moda.append(i)
    if len(moda) != len(datos):
        imprimir('Moda: ', moda)
    else:
        print('No hay moda')


import math


def percentile(data, perc: int):
    size = len(data)
    return sorted(data)[int(math.ceil((size * perc) / 100)) - 1]


with open('../heart_data_subsample.csv', newline='') as csvfile:
    lector_archivo = csv.DictReader(csvfile)
    edad_col = []
    genero_col = []
    altura_col = []
    peso_col = []
    sisto_col = []
    asist_col = []
    colest_col = []
    glucos_col = []
    con_tab_col = []
    con_alc_col = []
    act_fis_col = []
    result_col = []
    ## index,id,age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,cardio
    for fila in lector_archivo:
        edad_col.append(fila['age'])
        genero_col.append(fila['gender'])
        altura_col.append(fila['height'])
        peso_col.append(fila['weight'])
        sisto_col.append(fila['ap_hi'])
        asist_col.append(fila['ap_lo'])
        colest_col.append(fila['cholesterol'])
        glucos_col.append(fila['gluc'])
        con_tab_col.append(fila['smoke'])
        con_alc_col.append(fila['alco'])
        act_fis_col.append(fila['active'])
        result_col.append(fila['cardio'])
####
print("Estadisticas por columna sin librerias.\n")
print("\tColumna Edad en dias:")
media(edad_col)
moda(edad_col)
print("Q1 :" + percentile(edad_col, 25) + ", Q2 :" + percentile(edad_col, 50) + ", Q3 :" + percentile(edad_col, 75))
print("P10 :" + percentile(edad_col, 10) + ", P20 :" + percentile(edad_col, 20) + ", P90 :" + percentile(edad_col, 90))

print("\tColumna Genero: 2=Hombre,1=Mujer.")
moda(genero_col)
print(" ", Counter(genero_col))

print("\tColumna Altura en centimetros:")
media(altura_col)
moda(altura_col)
print(
    "Q1 :" + percentile(altura_col, 25) + ", Q2 :" + percentile(altura_col, 50) + ", Q3 :" + percentile(altura_col, 75))
print(
    "P2 :" + percentile(altura_col, 2) + ", P5 :" + percentile(altura_col, 5) + ", P30 :" + percentile(altura_col, 30))

print("\tColumna Peso en Kg:")
media(peso_col)
moda(peso_col)
print("Q1 :" + percentile(peso_col, 25) + ", Q2 :" + percentile(peso_col, 50) + ", Q3 :" + percentile(peso_col, 75))
print("P5 :" + percentile(peso_col, 5) + ", P15 :" + percentile(peso_col, 15) + ", P40 :" + percentile(peso_col, 40))

print("\tColumna Presion Sistolica:")
media(sisto_col)
moda(sisto_col)
print("Q1 :" + percentile(sisto_col, 25) + ", Q2 :" + percentile(sisto_col, 50) + ", Q3 :" + percentile(sisto_col, 75))
print("P9 :" + percentile(sisto_col, 9) + ", P18 :" + percentile(sisto_col, 18) + ", P45 :" + percentile(sisto_col, 45))

print("\tColumna Presion Asistolica:")
media(asist_col)
moda(asist_col)
print("Q1 :" + percentile(asist_col, 25) + ", Q2 :" + percentile(asist_col, 50) + ", Q3 :" + percentile(asist_col, 75))
print("P3 :" + percentile(asist_col, 3) + ", P21 :" + percentile(asist_col, 21) + ", P51 :" + percentile(asist_col, 51))

print("\tColumna Colesterol:")
moda(colest_col)
print(" ", Counter(colest_col))

print("\tColumna Glucosa :")
moda(glucos_col)
print(" ", Counter(glucos_col))

print("\tColumna Fumador 0 No, 1 Si.")
moda(con_tab_col)
print(" ", Counter(con_tab_col))

print("\tColumna Consumo de Alcohol 0 No, 1 Si.")
moda(con_alc_col)
print(" ", Counter(con_tab_col))

print("\tColumna Actividad fisica 0 No, 1 Si.")
moda(act_fis_col)
print(" ", Counter(act_fis_col))

print("\tColumna Resultado Enfermedad Cardiovacular 0 No, 1 Si.")
moda(result_col)
print(" ", Counter(result_col))

import numpy as np
import pandas as pd

dataset = pd.read_csv("../heart_data_subsample.csv")
dataset.describe()
print("Estadisticas por columna con numpy y pandas.\n")

print("Columna Edad: \n", dataset['age'].describe())
print("Columna Altura: \n", dataset.groupby('gender').height.describe())
print("Columna Peso: \n", dataset['weight'].describe())
print("Columna Sistolica: \n", dataset['ap_hi'].describe())
print("Columna Asistolica: \n", dataset['ap_lo'].describe())

print("Graficos por columnas.\n")
dataset.height.plot()
print("Fin.\n")


