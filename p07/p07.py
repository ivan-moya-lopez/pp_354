import csv
import random


def generar_indices():
    indices = []
    indices_unicos = []
    contador = 0
    limite = int(1700 * 0.78)

    while contador <= limite:
        indices.append(random.randint(1, 1700))
        contador += 1
    indices_unicos = list(dict.fromkeys(indices))
    indices_unicos.sort()
    return indices_unicos


# para el primer ciclo
indices = generar_indices()

with open('../heart_data_subsample.csv', newline='') as csvfile:
    data = {}
    train_data = {}
    test_data = {}
    lector_archivo = csv.reader(csvfile)
    for row in lector_archivo:
        data[row[0]] = {'age': row[1], 'gender': row[2], 'height': row[3], 'weight': row[4], 'ap_hi': row[5],
                        'ap_lo': row[6], 'cholesterol': row[7], 'gluc': row[8], 'smoke': row[9], 'alco': row[10],
                        'active': row[11], 'cardio': row[12]}
for i in range(len(indices)):
    if str(indices[i]) in data.keys():
        train_data[indices[i]] = data.get(str(indices[i]))

test_data = {key for key in data.keys() & train_data if data[key] != train_data[key]}

print(train_data.items())
print("test \n")
print(test_data)
# para el segundo ciclo
# print(len(generar_indices()))
# print(generar_indices())
