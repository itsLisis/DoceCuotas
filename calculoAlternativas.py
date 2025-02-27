import math
from sympy import symbols, Eq, nsolve
from model.flujosEfectivo import *

def mcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def alternativaPorTabla(TMAR, alternativaUno: list, alternativaDos: list) -> bool:
    """Retorna True si la alternativaUno es la adecuada. False en caso contrario"""
    minimoComunMultiplo = mcm(alternativaUno[3], alternativaDos[3])

    alternativas: list = [alternativaUno, alternativaDos]

    if (alternativaUno[0] > alternativaDos[0]):
        alternativas[1] = alternativaUno
        alternativas[0] = alternativaDos

    resultados: list = []

    valorA = 0
    valorB = 0
    for i in range(minimoComunMultiplo):
        if i == 0:
            # inversion
            valorA = -alternativas[0][0]
            valorB = -alternativas[1][0]
            resultados.append(valorB - valorA)
            continue

        if i % alternativas[0][3] != 0:
            # costo de operacion
            valorA = -alternativas[0][1]
        else:
            # costo de operacion
            valorA = -alternativas[0][1]
            # valor rescate
            valorA += alternativas[0][2]
            # inversion
            valorA += -alternativas[0][0]

        if i % alternativas[1][3] != 0:
            # costo de operacion
            valorB = -alternativas[1][1]
        else:
            # costo de operacion
            valorB = -alternativas[1][1]
            # valor rescate
            valorB += alternativas[1][2]
            # inversion
            valorB += -alternativas[1][0]

        resultados.append(valorB - valorA)

        if i == (minimoComunMultiplo - 1):
            # costo de operacion
            valorA = -alternativas[0][1]
            # valor rescate
            valorA += alternativas[0][2]
            # costo de operacion
            valorB = -alternativas[1][1]
            # valor rescate
            valorB += alternativas[1][2]
            resultados.append(valorB - valorA)

    # DESPEJAR I
    i = symbols('i')
    expr = sum(x_k / (1 + i) ** k for k, x_k in enumerate(resultados))

    solucion = nsolve(Eq(expr, 0), 0.07) * 100
    print(solucion)

    print(f"A: {alternativas[0][0]}, B: {alternativas[1][0]}")
    # for i in range(len(resultados)):
    #     print(resultados[i])
    # print(sum(resultados))

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




alternativaUno: list = []
alternativaDos: list = []

# Indice de la lsita:
# 0: costoInicial
# 1: costoOperacionAnual
# 2: valorRescate
# 3: vidaUtil

# Ejerciio tabla
alternativaUno.append(18000)
alternativaUno.append(4000)
alternativaUno.append(1000)
alternativaUno.append(3)

alternativaDos.append(35000)
alternativaDos.append(3600)
alternativaDos.append(2700)
alternativaDos.append(6)

# Ejercicio taller RC
# alternativaUno.append(40000)
# alternativaUno.append(10000)
# alternativaUno.append(12000)
# alternativaUno.append(3)

# alternativaDos.append(65000)
# alternativaDos.append(12000)
# alternativaDos.append(25000)
# alternativaDos.append(6)


interes = 20
# interes = 15
resultados: list = []

print(alternativaPorTabla(interes, alternativaUno, alternativaDos))

# print(alternativaPorRC(interes, alternativaUno, alternativaDos, resultados))
# print(f"Resultado AlternativaUno: {resultados[0]}\nResultado AlternativaDos: {resultados[1]}")


