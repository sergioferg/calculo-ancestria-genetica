import matplotlib.pyplot as plt
import numpy as np
import csv

N = 30
M = 100

datos_genotipo = []

with open('datos_genotipo.csv', newline='') as csv_datos:
    datos_reader = csv.reader(csv_datos, delimiter=',')
    datos_genotipo = list(datos_reader)

individuos = []

for i, dato in enumerate(datos_genotipo):
    if i == 0:
        continue
    individuos.append(dato[1:]) 

individuos = np.array(individuos, dtype=int)

frecuencias_alelo = []

for j in range(0, M):
    frecuencia = sum(individuos[:, j]) / (2*N)
    frecuencias_alelo.append(frecuencia)

normalizado_patterson = []

for i in range(0, N):
    normal = []
    for j in range (0, M):
        p = frecuencias_alelo[j]

        if p == 0 or p == 1:
            normal.append(0)
        else:
            num = individuos[i][j] - 2*frecuencias_alelo[j]
            den = np.sqrt(2*p*(1-p))
            normal.append(num/den)
        
    normalizado_patterson.append(normal)

normalizado_patterson = np.array(normalizado_patterson)
u, s, vt = np.linalg.svd(normalizado_patterson)
        