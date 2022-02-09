import sys


def peso_molecular(pars: dict) -> float:
    """
    Toma un diccionario de una fórmula parseada y calcula su peso molecular

    Args:
        pars (dict): diccionario producto de la funcion parsear_formula(formula)

    Returns:
        float: peso molecular calculado
    """
    C = 12.0107
    H = 1.00784
    O = 15.999
    N = 14.0067
    P = 30.973762
    B = 10.811

    peso_molecular = 0

    peso_molecular = pars['C'] * C + pars['H'] * H + pars['O'] * O + pars['N'] * N + pars['P'] * P + pars['B'] * B
    return peso_molecular


def parsear_formula(formula: str) -> dict:
    """
    Función que recibe un string de una fórmula y devuelve la cant. de elementos que la componen

    Args:
        formula (str): fórmula molecular, ej: 'C6H12O6'

    Returns:
        dict: devuelve diccionario con la cantidad de cada elemento
    """
    elementos = 'CHONPB'

    res = {
        'C': 0,
        'H': 0,
        'O': 0,
        'N': 0,
        'P': 0,
        'B': 0
    }
    for nletra, letra in enumerate(formula.upper()):
        if letra in elementos:
            if nletra < len(formula) - 1 and formula[nletra + 1:nletra + 3].isdigit():
                res[letra] += int(formula[nletra + 1:nletra + 3])
            elif nletra < len(formula) - 1 and formula[nletra + 1].isdigit():
                res[letra] += int(formula[nletra + 1])
            else:
                res[letra] += 1
    return res


def conv_aldononitrilo_acetilado(peso: float, aldosa: dict, deoxi: int = 0) -> float:
    """
    Convierte PM de aldosa a su aldononitrilo peracetilado

    Args:
        peso (float): PM de la aldosa
        aldosa (dict): diccionario parseado con 'parsear_formula': tiene la cant de cada elemento
        deoxi (int, optional): número de deoxi en la molécula. Defaults to 0.

    Returns:
        float: PM del aldononitrilo peracetilado
    """
    pm = peso - 3 + (aldosa['C'] - 1 - deoxi) * 42.03

    return pm


def conv_alditol_acetilado(peso: float, aldosa: dict, deoxi: int = 0) -> float:
    """
    Convierte PM de aldosa a su alditol peracetilado

    Args:
        peso (float): PM de la aldosa
        aldosa (dict): diccionario parseado con 'parsear_formula': tiene la cant de cada elemento
        deoxi (int, optional): número de deoxi en la molécula. Defaults to 0.

    Returns:
        float: PM del alditol peracetilado
    """

    pm = peso + 44.05 + (aldosa['C'] - 1 - deoxi) * 42.03

    return pm


def main(argumentos: list):
    """
    Aplicación que calcula pesos moleculares de compuestos a partir de sus fórmulas.
    Es posible calcular además los PM de sus alditoles y sus aldononitrilos peracetilados.

    Sintaxis programa: <Formula molecular> <ARGUMENTOS>

    Argumentos posibles:
    * pm -> Da el peso molecular de la formula ingresada
        ? Ej: python pm.py c6h12o6 pm
        ? Esto devuelve el peso molecular de la fórmula tal cual fue pasada
    * info -> Da el PM de la formula y tmbn de su alditol/aldonitrilo peracetilado
        ? Ej: python pm.py c6h12o6 info
        ? Esto devuelve los PM de la fórmula, de su alditol perAc y su aldononitrilo perAc
    * deoxi -> Da el PM de la formula y tmbn de su alditol/aldonitrilo peracetilado CON UN DEOXI
        ? Ej: python pm.py c6h12o6 deoxi
        ? Esto devuelve los PM de la fórmula, de su alditol perAc y su aldononitrilo perAc CON UN DEOXI

    Args:
        argumentos (list): lista de argumentos pasados por sys.argv
    """

    if len(argumentos) == 2 and argumentos[1] == 'pm':
        formula = argumentos[0]
        peso = peso_molecular(parsear_formula(formula))
        print(f'Fórmula molecular: {formula.upper()}\nPM: {peso:.2f}.')

    elif len(argumentos) >= 2 and argumentos[1] == 'alditol':
        deoxi = 0
        formula = argumentos[0]
        parseado = parsear_formula(formula)
        peso = peso_molecular(parseado)
        if len(argumentos) == 3:
            deoxi = int(argumentos[2])
            alditol_per = conv_alditol_acetilado(peso, parseado, deoxi)
        else:
            alditol_per = conv_alditol_acetilado(peso, parseado)
        print(f'Fórmula molecular: {formula.upper()}\nPM: {peso:.2f}\nNº de deoxis: {deoxi}\nPM alditol peracetilado: {alditol_per:.2f}.')

    elif len(argumentos) >= 2 and argumentos[1] == 'aldono':
        deoxi = 0
        formula = argumentos[0]
        parseado = parsear_formula(formula)
        peso = peso_molecular(parseado)
        if len(argumentos) == 3:
            deoxi = int(argumentos[2])
            aldono_per = conv_aldononitrilo_acetilado(peso, parseado, deoxi)
        else:
            aldono_per = conv_aldononitrilo_acetilado(peso, parseado)
        print(f'Fórmula molecular: {formula.upper()}\nPM: {peso:.2f}\nNº de deoxis: {deoxi}\nPM aldononitrilo peracetilado: {aldono_per:.2f}.')


if __name__ == "__main__":
    main(sys.argv[1:])
