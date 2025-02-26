def calcularPorcentaje(interes) -> float:
    return interes / 100

# Cantidad Unica
def futuroDadoPresente(valorPresente, interes, periodos):
    interes = calcularPorcentaje(interes)
    return round(valorPresente * ( (1 + interes)**periodos ),3)


def presenteDadoFuturo(valorFuturo, interes, periodos):
    interes = calcularPorcentaje(interes)
    return round(valorFuturo / ( (1 + interes)**periodos ),3)

# Serie Uniforme Presente
def presenteDadoAnualidad(valorAnualidad, interes, periodos):
    interes = calcularPorcentaje(interes)
    return round(valorAnualidad * ( ( (1 + interes)**periodos - 1 ) / ( interes * (1 + interes)**periodos) ),3)

def anualidadDadoPresente(valorPresente, interes, periodos):
    interes = calcularPorcentaje(interes)
    return round(valorPresente * ( ( interes * (1 + interes)**periodos ) / ( (1 + interes)**periodos - 1 )),3)

# Serie Uniforme Futuro
def futuroDadoAnualidad(valorAnualidad, interes, periodos):
    interes = calcularPorcentaje(interes)
    return round(valorAnualidad * ( ( (1 + interes)**periodos - 1 ) / ( interes ) ),3)

def anualidadDadoFuturo(valorFuturo, interes, periodos):
    interes = calcularPorcentaje(interes)
    return round(valorFuturo * ( ( interes ) / ( (1 + interes)**periodos - 1 ) ),3)

# Gradiente Aritmetico
def presenteDadoGradienteAritmetico(valorGradienteAritmetico, interes, periodos):
    interes = calcularPorcentaje(interes)
    return round(valorGradienteAritmetico * ( 
                                        ( (1 + interes)**periodos - (interes * periodos) - 1 ) /
                                        ( interes**2 * (1 + interes)**periodos ) 
                                        ),3)

def anualidadDadoGradienteAritmetico(gradiente, interes, periodos):
    interes = calcularPorcentaje(interes)
    return round(gradiente * ( (1 / interes) - ( periodos / ( (1 + interes)**periodos - 1) ) ),3)

# Gradiente Geometrico
def presenteDadoGradienteGeometrico(valorPrimerPago, tasaDeCambio, interes, periodos):
    interes = calcularPorcentaje(interes)
    tasaDeCambio = calcularPorcentaje(tasaDeCambio)

    if tasaDeCambio != interes:
        return round(
            valorPrimerPago * ( (1 - ((1 + tasaDeCambio) / (1 + interes))**periodos) / (interes - tasaDeCambio) ), 3)
    elif tasaDeCambio == interes:
        return round(( valorPrimerPago * (periodos / (1+interes)) ), 3)


# Tests
def test_formulas_financieras():
    # Cantidad Única
    assert futuroDadoPresente(100, 10, 1) == 110.000, "Error en futuroDadoPresente"
    assert presenteDadoFuturo(110, 10, 1) == 100.000, "Error en presenteDadoFuturo"

    # Serie Uniforme Presente
    assert presenteDadoAnualidad(100, 10, 5) == 379.079, "Error en presenteDadoAnualidad"
    assert anualidadDadoPresente(379.079, 10, 5) == 100.000, "Error en anualidadDadoPresente"

    # Serie Uniforme Futuro
    assert futuroDadoAnualidad(100, 10, 5) == 610.510, "Error en futuroDadoAnualidad"
    assert anualidadDadoFuturo(610.510, 10, 5) == 100.000, "Error en anualidadDadoFuturo"

    # Gradiente Aritmético
    assert presenteDadoGradienteAritmetico(100, 10, 5) == 686.180, "Error en presenteDadoGradienteAritmetico"
    assert anualidadDadoGradienteAritmetico(100, 10, 5) == 181.013, "Error en anualidadDadoGradienteAritmetico"

    # Gradiente Geométrico (g != i)
    assert presenteDadoGradienteGeometrico(100, 5, 10, 5) == 415.059, "Error en presenteDadoGradienteGeometrico (g ≠ i)"
    
    # Gradiente Geométrico (g = i)
    assert presenteDadoGradienteGeometrico(100, 10, 10, 5) == 454.545, "Error en presenteDadoGradienteGeometrico (g = i)"
    
    print("¡Todos los tests pasaron exitosamente!")

# Ejecutar los tests
#test_formulas_financieras()