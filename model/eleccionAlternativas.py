import math
from sympy import symbols, Eq, nsolve
from model.flujosEfectivo import *

def mcm(a, b):
    a = int(a)
    b = int(b)
    return abs(a * b) // math.gcd(a, b)


def alternativaPorTabla(TMAR, alternativaUno: list, alternativaDos: list, interesAproximado: list) -> bool:
    """Retorna True si la alternativaUno es la adecuada. False en caso contrario"""
    minimoComunMultiplo = mcm(alternativaUno[3], alternativaDos[3])

    alternativas: list = [alternativaUno, alternativaDos]

    if (alternativaUno[0] > alternativaDos[0]):
        alternativas[1] = alternativaUno
        alternativas[0] = alternativaDos

    resultados: list = []

    # Inversión inicial
    valorA = -alternativas[0][0]
    valorB = -alternativas[1][0]
    resultados.append(valorB - valorA)

    for i in range(1, minimoComunMultiplo):
        valorA = -alternativas[0][1]  # Costo de operación
        if i % alternativas[0][3] == 0:
            valorA += alternativas[0][2] - alternativas[0][0]  # Valor rescate e inversión
        
        valorB = -alternativas[1][1]  # Costo de operación
        if i % alternativas[1][3] == 0:
            valorB += alternativas[1][2] - alternativas[1][0]  # Valor rescate e inversión
        
        resultados.append(valorB - valorA)
    
    valorA = -alternativas[0][1] + alternativas[0][2]  # Último costo + rescate
    valorB = -alternativas[1][1] + alternativas[1][2]  # Último costo + rescate
    resultados.append(valorB - valorA)

    # DESPEJAR I
    i = symbols('i')
    expr = sum(x_k / (1 + i) ** k for k, x_k in enumerate(resultados))

    solucion = nsolve(Eq(expr, 0), 0.1) * 100
    print(solucion)

    print(f"A: {alternativas[0][0]}, B: {alternativas[1][0]}")
    # for i in range(len(resultados)):
    #     print(resultados[i])
    # print(sum(resultados))

    interesAproximado.append(solucion)

    if solucion < TMAR:
        return alternativas[0][0] == alternativaUno[0]
    else:
        return False


def alternativaPorRC(interes, alternativaUno: list, alternativaDos: list, listaResultados: list) -> bool:
    """Retorna True si la alternativaUno es la adecuada. False en caso contrario"""

    RC = anualidadDadoPresente(alternativaUno[0], interes, alternativaUno[3])
    RC -= anualidadDadoFuturo(alternativaUno[2], interes, alternativaUno[3])
    valorAnual = -RC - alternativaUno[1]

    listaResultados.append(round(valorAnual, 3))

    RC = anualidadDadoPresente(alternativaDos[0], interes, alternativaDos[3])
    RC -= anualidadDadoFuturo(alternativaDos[2], interes, alternativaDos[3])
    valorAnual = -RC - alternativaDos[1]

    listaResultados.append(round(valorAnual, 3))

    if (listaResultados[0] < 0 and listaResultados[1] < 0):
        return (listaResultados[0] > listaResultados[1])

    return (listaResultados[0] < listaResultados[1])
