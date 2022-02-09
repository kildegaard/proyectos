import serial
import time
from pprint import pprint

arduino = serial.Serial("COM3", 9600)
time.sleep(1)

elementos = []

while True:
    with open('log.csv', 'at') as log:
        linea = arduino.readline().decode('ascii').strip()
        print(linea, file=log)

        lista = linea.split(',')

        dic = {
            'A0': lista[0],
            'A1': lista[1],
            'A2': lista[2],
            'A3': lista[3]
        }
        elementos.append(dic)

    str = f'A0\tA1\tA2\tA3'
    print(str)
    print('='*(len(str)+3*5))
    print(f"{dic['A0']}\t{dic['A1']}\t{dic['A2']}\t{dic['A3']}")
    print("")
