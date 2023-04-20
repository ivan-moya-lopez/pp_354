import csv
import random

with open('../heart_data_subsample.csv', newline='') as csvfile:
    lector_archivo = csv.DictReader(csvfile)
encabezados = ['id', 'age', 'gender', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco',
               'active', 'cardio']
def generar_indices():
    indices = []
    indices_unicos = []
    contador = 0
    limite = int(1700 * 0.78)

    while contador <= limite:
        indices.append(random.randint(1, 1700))
        contador += 1
    indices_unicos = list(dict.fromkeys(indices))
    return indices_unicos
#para el primer ciclo
print(len(generar_indices()))
print(generar_indices())

#para el segundo ciclo
print(len(generar_indices()))
print(generar_indices())

