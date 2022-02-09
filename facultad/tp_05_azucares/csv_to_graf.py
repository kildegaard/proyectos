# Vamos a levantar csv y graficar

from matplotlib import pyplot as plt
import csv

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

plt.title('Ensayo de compresión - F vs dist')
plt.ylabel('Fuerza [N]')
plt.xlabel('Distancia [mm]')
for dato in datos:
    plt.scatter(*dato, marker='^', s=12)
plt.show()
