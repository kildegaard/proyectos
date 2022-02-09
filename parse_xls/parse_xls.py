# Vamos a tratar de parsear un excel para quedarnos con lo que queremos y convertirlo a csv

import xlrd
import sys

def abrir_excel(file, sheet):
    workbook = xlrd.open_workbook(file)
    hoja = workbook.sheet_by_name(sheet)
    return hoja


def headers(hoja, fila, desde, hasta):
    """
    Parseo el header, si lo hubiera
    Devuelvo una lista con los elementos
    """
    header = []
    for elemento in range(desde, hasta + 1):
        header.append(hoja.cell(fila, elemento).value)
    return header


def datos(hoja, fil_desde, fil_hasta, col_desde, col_hasta):
    """
    Parseo la data que me interesa
    Devuelvo una lista con los elementos
    """
    lineas = []
    for fila in range(fil_desde, fil_hasta + 1):
        valores = []
        for columna in range(col_desde, col_hasta + 1):
            try:
                valores.append(str(hoja.cell(fila, columna).value))
            except:
                pass
        lineas.append(valores)
    return lineas


def parsear_csv(datos, arch_salida = 'salida.csv', headers = None):
    with open(arch_salida+'.csv', 'wt') as f:
        if headers:
            h = ','.join(headers)
            print(h, file = f)
        for linea in datos:
            print(','.join(linea), file = f)

def main(args):

    if len(args) == 1:
        raise SystemExit("Modo de uso: %s file.xls nombre_hoja fil_desde fil_hasta col_desde col_hasta [fila, desde, hasta]\nLos primeros 4 numeros son sobre los datos (empezando en 0) y los ultimos 3, opcionales, sobre el header" % args[0])
    file = args[1]
    sheet = args[2]
    fil_desde = int(args[3])
    fil_hasta = int(args[4])
    col_desde = int(args[5])
    col_hasta = int(args[6])

    if len(args) == 10:
        fila = int(args[7])
        desde = int(args[8])
        hasta = int(args[9])

    hoja = abrir_excel(file, sheet)
    cuerpo = datos(hoja, fil_desde, fil_hasta, col_desde, col_hasta)
    if len(args) == 10:
        head = headers(hoja, fila, desde, hasta)
    else:
        head = None
    parsear_csv(cuerpo, sheet, head)

if __name__ == '__main__':
    main(sys.argv)
