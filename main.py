import matplotlib.pyplot as plt
import numpy as np
import csv

datos_genotipo = []

with open('datos_genotipo.csv', newline='') as csv_datos:
    datos_reader = csv.reader(csv_datos, delimiter=',')
    datos_genotipo = list(datos_reader)

individuos = []

for i, dato in enumerate(datos_genotipo):
    if i == 0:
        continue
    individuos.append(dato[1:]) 
