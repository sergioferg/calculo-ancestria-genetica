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

PC = u * s
PC1 = PC[:, 0]
PC2 = PC[:, 1]

import matplotlib.pyplot as plt
import numpy as np
import csv
import seaborn as sns

N = 30
M = 100

datos_genotipo = []

with open('datos_genotipo.csv', newline='') as csv_datos:
    datos_reader = csv.reader(csv_datos, delimiter=',')
    datos_genotipo = list(datos_reader)

individuos = []

poblaciones_texto = []


for i, dato in enumerate(datos_genotipo):
    if i == 0:
        continue
    individuos.append(dato[1:])
    poblaciones_texto.append(dato[0])

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

PC = u * s
PC1 = PC[:, 0]
PC2 = PC[:, 1]

plt.figure()


grupos_por_posicion = np.where(PC1 > 2, 'Ancestral B', 
                               np.where(PC1 < -2, 'Ancestral A', 'Mezcla'))
colores_poblacion = {
    'Ancestral A': '#FF0000', # Rojo
    'Ancestral B': '#0000FF', # Azul
    'Mezcla': '#800080'       # Morado
}

sns.scatterplot(
    x=PC1, 
    y=PC2, 
    hue=grupos_por_posicion, 
    palette=colores_poblacion,
    s=70, 
)

plt.title("Mapa de Ancestría Genética: PC1 vs PC2")
plt.xlabel(f"PC1")
plt.ylabel(f"PC2")

plt.grid(color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
plt.axhline(0, color='k', linewidth=1, linestyle='-', alpha=0.3)
plt.axvline(0, color='k', linewidth=1, linestyle='-', alpha=0.3)
plt.legend(title="Poblaciones")
plt.savefig("mapa_ancestria_colores.pdf") 
plt.show()
        
