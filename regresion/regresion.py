
''' Para usar esta función lineal desde importar:

    1. Importar
    2. resultado = lineal(X, Y)
        a. Acá ya tenés todos los datos (pendiente, ordenada, error)
    3. Para graficar:
        a. grafico(X, Y, resultado)
'''


import sys
import random
import csv
import matplotlib.pyplot as plt


def lineal(X: list, Y: list) -> None:
    """Regresión lineal. Acepta lista X y lista Y y devuelve m y box

    Args:
        X (list): Valores de x
        Y (list): Valores de y

    Returns:
        float, float: m, b
    """
    def calc_error(y_medido, y_estimado):
        SSE = sum([(y - ys)**2 for y, ys in zip(y_medido, y_estimado)])
        SST = sum([(y - prom(y_medido))**2 for y in y_medido])
        r2 = 1 - (SSE / SST)
        return r2

    x_prom = prom(X)
    y_prom = prom(Y)

    Sxy = sum([(x - x_prom) * (y - y_prom) for x, y in zip(X, Y)])
    Sxx = sum([(x - x_prom)**2 for x in X])

    m = Sxy / Sxx
    b = prom(Y) - m * prom(X)

    y_estimado = [m * x + b for x in X]

    error = calc_error(Y, y_estimado)

    res = {
        'pendiente': m,
        'ordenada': b,
        'ys': y_estimado,
        'error': error
    }

    return res


def impresion(reg):
    print(f'Regresión lineal - Y = {reg["pendiente"]:0.3f}x + {reg["ordenada"]:0.3f} | R2: {reg["error"]:0.3f}')


def prom(a):
    return sum(a) / len(a)

# TODO: Detalle que encontré. Cuando le sacás puntos al gráfico para poder "encontrar una recta"
# TODO: te pasa que no coinciden en tamaño X y reg['ys'], hay que ver como arreglar


def grafico(X, Y, reg=None):
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Gráfico Y vs X')
    plt.scatter(X, Y)
    if reg:
        plt.plot(X, reg['ys'], color='red', linestyle=':', label='Regresión lineal')
        plt.legend(loc='upper left')
        if reg['ordenada'] >= 0:
            plt.text(max(X) * 0.74, max(Y) * 0.20, f'Y = {reg["pendiente"]:.3f}x + {abs(reg["ordenada"]):.3f}\n$R^2$={reg["error"]:.3f}')
        else:
            plt.text(max(X) * 0.74, max(Y) * 0.20, f'Y = {reg["pendiente"]:.3f}x - {abs(reg["ordenada"]):.3f}\n$R^2$={reg["error"]:.3f}')
    plt.grid()
    plt.show()


def main(args):
    if len(args) == 1:
        print('Demostración de como funciona')

        X = [i for i in range(10)]
        error = [random.normalvariate(0, 1.5) for i in range(len(X))]
        Y = [((2.5 * x + 0.35) + er) for x, er in zip(X, error)]

    elif len(args) == 2:
        X = []
        Y = []
        with open(args[1], 'rt') as f:
            lineas = csv.reader(f)
            for nlinea, linea in enumerate(lineas, start=1):
                try:
                    Y.append(float(linea[1]))
                    X.append(float(linea[0]))
                except:
                    print(f'Problema en la linea {nlinea}')
                    pass
    else:
        raise SystemExit('Uso: %s archivo.csv' % args[0])

    res = lineal(X, Y)
    impresion(res)
    grafico(X, Y, res)


if __name__ == "__main__":
    main(sys.argv)
