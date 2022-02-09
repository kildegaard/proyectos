#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 12:53:49 2020

@author: gus
"""

# Mandamos los import, cargamos los datos de los .csv en `datos`
from matplotlib import pyplot as plt
import csv
import math
import regresion

plt.style.use('seaborn')

muestras = ['Muestra 1.csv', 'Muestra 2.csv']
datos = []
for muestra in muestras:
    with open(muestra) as f1:
        lineas = csv.reader(f1)
        header = next(lineas)
        x = []
        y = []
        for linea in lineas:

            x.append(float(linea[0]))
            y.append(float(linea[1]))
        datos.append((x, y))
# %%
colores = ['green', 'blue']
labels = ['Muestra', 'Duplicado']

plt.title('Ensayo de compresión - F vs dist', fontsize=15)
plt.ylabel('Fuerza [N]', fontsize=15)
plt.xlabel('Distancia [mm]', fontsize=15)
for dato, lab, col in zip(datos, labels, colores):
    plt.scatter(*dato, marker='o', s=12, label=lab, c=col)
plt.legend(loc='lower right', fontsize=15)
# plt.show()
# %%

# Ahora vamos a corregir los datos de fuerza (𝐹) y distancia (ℎ) para convertirlos en esfuerzo (𝜎) y deformación relativa(𝜖) dividiéndolos
# por el área de la sección transversal inicial de la muestra (𝐴0) y por la altura inicial de la misma (ℎ0).

h_0 = 20
A_0 = (math.pi / 4) * (0.02) ** 2

muestra_1 = datos[0]
muestra_2 = datos[1]

m1_x, m1_y = muestra_1
m2_x, m2_y = muestra_2

m1_x = [i / h_0 for i in m1_x]
m1_y = [i / A_0 for i in m1_y]

m2_x = [i / h_0 for i in m2_x]
m2_y = [i / A_0 for i in m2_y]

# %%

# Graficamos la versión corregida para la Muestra 1

plt.grid(zorder=3)
plt.title('Ensayo de compresión - $\sigma$ vs $\epsilon$', fontsize=15)
plt.xlabel('Deformación relativa $\epsilon$', fontsize=15)
plt.ylabel('Esfuerzo $\sigma$ [Pa]', fontsize=15)
plt.scatter(m1_x, m1_y, zorder=2, s=5, c='green', label='Muestra')
plt.ylim(bottom=0, top=25000)
plt.legend(loc='upper left', fontsize=15)

# %%

# Graficamos la versión corregida para la Muestra 2

plt.grid(zorder=3)
plt.title('Ensayo de compresión - $\sigma$ vs $\epsilon$', fontsize=15)
plt.xlabel('Deformación relativa $\epsilon$', fontsize=15)
plt.ylabel('Esfuerzo $\sigma$ [Pa]', fontsize=15)
plt.scatter(m2_x, m2_y, zorder=1, s=5, c='blue', label='Duplicado')
plt.ylim(bottom=0, top=25000)
plt.legend(loc='upper left', fontsize=15)

# %%

# Creamos una función para encontrar dónde comienza la parte lineal


def inicio_pendiente(dato_x, dato_y, paso=5):
    pend_anterior = 0
    contador = 0
    for i in range(len(dato_x) - paso):
        pend_actual = (dato_y[i + paso] - dato_y[i]) / (dato_x[i + paso] - dato_x[i])
#         print(pend_actual)
        if pend_actual > pend_anterior:
            pend_anterior = pend_actual
        else:
            contador += 1
        if contador == 10:
            return i

# %%


pend_m1 = inicio_pendiente(m1_x, m1_y, 15)
pend_m2 = inicio_pendiente(m2_x, m2_y, 15)
print(f'Inicio de pendiente en Muestra 1: índice {pend_m1}')
print(f'Inicio de pendiente en Muestra 2: índice {pend_m2}')

# %%

# Acá tenemos los parámetros para trabajar el resto de las cosas

# Acá tenemos los parámetros para trabajar el resto de las cosas

recta_m1 = regresion.lineal(m1_x[145:200], m1_y[145:200])
print(f'Muestra 1\nPendiente: {recta_m1["pendiente"]:.3f} ± {recta_m1["delta_pendiente"]:.2f}\nOrdenada: {recta_m1["ordenada"]:.3f} ± {recta_m1["delta_ordenada"]:.2f}\nR2: {recta_m1["r2"]:.3f}')

recta_m2 = regresion.lineal(m2_x[145:200], m2_y[145:200])
print(f'Muestra 2\nPendiente: {recta_m2["pendiente"]:.3f} ± {recta_m2["delta_pendiente"]:.2f}\nOrdenada: {recta_m2["ordenada"]:.3f} ± {recta_m2["delta_ordenada"]:.2f}\nR2: {recta_m2["r2"]:.3f}')
# %%

# Pero antes vamos a sacar los gráficos bien lindos

x_recta_m1 = m1_x[100:250]
y_recta_m1 = [recta_m1['pendiente'] * x + recta_m1['ordenada'] for x in x_recta_m1]

plt.title('Ensayo de compresión - $\sigma$ vs $\epsilon$', fontsize=15)
plt.xlabel('Deformación relativa $\epsilon$', fontsize=15)
plt.ylabel('Esfuerzo $\sigma$ [Pa]', fontsize=15)

plt.plot(m1_x, m1_y, color='green', label='Muestra')
plt.plot(x_recta_m1, y_recta_m1, color='red', label='Regresión lineal')

if recta_m1['ordenada'] >= 0:
    plt.text(max(m1_x) * 0.6, max(m1_y) * 0.06, f'Y = {recta_m1["pendiente"]:.3f}x + {abs(recta_m1["ordenada"]):.3f}\n$R^2$={recta_m1["r2"]:.3f}', fontsize=15)
else:
    plt.text(max(m1_x) * 0.6, max(m1_y) * 0.06, f'Y = {recta_m1["pendiente"]:.3f}x - {abs(recta_m1["ordenada"]):.3f}\n$R^2$={recta_m1["r2"]:.3f}', fontsize=15)
plt.ylim(bottom=0, top=25000)
plt.legend(loc='upper left', fontsize=15)

# %%

x_recta_m2 = m2_x[100:220]
y_recta_m2 = [recta_m2['pendiente'] * x + recta_m2['ordenada'] for x in x_recta_m2]

plt.grid(zorder=3)
plt.title('Ensayo de compresión - $\sigma$ vs $\epsilon$', fontsize=15)
plt.xlabel('Deformación relativa $\epsilon$', fontsize=15)
plt.ylabel('Esfuerzo $\sigma$ [Pa]', fontsize=15)

plt.plot(m2_x, m2_y, color='blue', label='Duplicado')
plt.plot(x_recta_m2, y_recta_m2, color='red', label='Regresión lineal')

if recta_m2['ordenada'] >= 0:
    plt.text(max(m2_x) * 0.6, max(m2_y) * 0.06, f'Y = {recta_m2["pendiente"]:.3f}x + {abs(recta_m2["ordenada"]):.3f}\n$R^2$={recta_m2["r2"]:.3f}', fontsize=15)
else:
    plt.text(max(m2_x) * 0.6, max(m2_y) * 0.06, f'Y = {recta_m2["pendiente"]:.3f}x - {abs(recta_m2["ordenada"]):.3f}\n$R^2$={recta_m2["r2"]:.3f}', fontsize=15)

plt.ylim(bottom=0, top=25000)
plt.legend(loc='upper left', fontsize=15)

# %%


def max_funcion(dato_y):
    maximo = max(dato_y)
    indice = dato_y.index(maximo)
    return indice, maximo


# %%
index_max_m1 = max_funcion(m1_y)[0]
index_max_m2 = max_funcion(m2_y)[0]

# %%
plt.plot(m1_x, m1_y)
plt.ylim(bottom=0, top=25000)
plt.axvline(m1_x[index_max_m1])

# %%
plt.plot(m2_x, m2_y)
plt.axvline(m2_x[index_max_m2])

# %%
esfuerzo_m1 = max_funcion(m1_y)[1]
esfuerzo_m2 = max_funcion(m2_y)[1]

defor_m1 = m1_x[max_funcion(m1_y)[0]]
defor_m2 = m2_x[max_funcion(m2_y)[0]]

firmeza_m1 = esfuerzo_m1 / defor_m1
firmeza_m2 = esfuerzo_m2 / defor_m2

datos = (('Esfuerzo', esfuerzo_m1, esfuerzo_m2), ('Deformación', defor_m1, defor_m2), ('Firmeza', firmeza_m1, firmeza_m2))

# %%
headers = ('', 'Muestra 1', 'Muestra 2')
print('%12s %12s %12s' % headers)

print(('-' * 12 + ' ') * len(headers))

for fila in datos:
    #     print('%10s %10.2f %10.2f' % fila)
    print(f'{fila[0]:>12s}{fila[1]:>12.2f}{fila[2]:>12.2f}')

# %%
