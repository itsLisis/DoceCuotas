valorPresente: float
valorFuturo: float

valorAnualidad: float

valorGradienteAritmetico: float
valorGradienteGeometrico: float
valorPrimerPago: float

interes: float
periodos: float

# Cantidad Unica
def futuroDadoPresente(valorPresente, interes, periodos):
    return round(valorPresente * ( (1 + interes)**periodos ),3)


def presenteDadoFuturo(valorFuturo, interes, periodos):
    return round(valorFuturo / ( (1 + interes)**periodos ),3)

# Serie Uniforme Presente
def presenteDadoAnualidad(valorAnualidad, interes, periodos):
    return round(valorAnualidad * ( ( (1 + interes)**periodos - 1 ) / ( interes * (1 + interes)**periodos) ),3)

def anualidadDadoPresente(valorPresente, interes, periodos):
    return round(valorPresente * ( ( interes * (1 + interes)**periodos ) / ( (1 + interes)**periodos - 1 )),3)

# Serie Uniforme Futuro
def futuroDadoAnualidad(valorAnualidad, interes, periodos):
    return round(valorAnualidad * ( ( (1 + interes)**periodos - 1 ) / ( interes ) ),3)

def anualidadDadoFuturo(valorFuturo, interes, periodos):
    return round(valorFuturo * ( ( interes ) / ( (1 + interes)**periodos - 1 ) ),3)

# Gradiente Aritmetico
def presenteDadoGradienteAritmetico(valorGradienteAritmetico, interes, periodos):
    return round(valorGradienteAritmetico * ( 
                                        ( (1 + interes)**periodos - (interes * periodos) - 1 ) /
                                        ( interes**2 * (1 + interes)**periodos ) 
                                        ),3)

def anualidadDadoGradienteAritmetico(valorGradienteAritmetico, interes, periodos):
    return round(valorGradienteAritmetico * ( (1 / interes) - ( periodos / ( (1 + interes)**periodos - 1) ) ),3)

# Gradiente Geometrico
def presenteDadoGradienteGeometrico(valorPrimerPago, valorGradienteGeometrico, interes, periodos):
    if valorGradienteGeometrico != interes:
        return round(( 
                            ( valorPrimerPago * (1 - ((1+valorGradienteGeometrico)/(1+interes))**periodos)) / (interes - valorGradienteGeometrico) 
                        ),3)
    elif valorGradienteGeometrico == interes:
        return round(( valorPrimerPago * (periodos / (1+interes)) ),3)


# Tests
def test_formulas_financieras():
    # Cantidad Única
    assert round(futuroDadoPresente(100, 0.1, 1), 3) == 110.000, "Error en futuroDadoPresente"
    assert round(presenteDadoFuturo(110, 0.1, 1), 3) == 100.000, "Error en presenteDadoFuturo"

    # Serie Uniforme Presente
    assert round(presenteDadoAnualidad(100, 0.1, 5), 3) == 379.079, "Error en presenteDadoAnualidad"
    assert round(anualidadDadoPresente(379.079, 0.1, 5), 3) == 100.000, "Error en anualidadDadoPresente"

    # Serie Uniforme Futuro
    assert round(futuroDadoAnualidad(100, 0.1, 5), 3) == 610.510, "Error en futuroDadoAnualidad"
    assert round(anualidadDadoFuturo(610.510, 0.1, 5), 3) == 100.000, "Error en anualidadDadoFuturo"

    # Gradiente Aritmético
    assert round(presenteDadoGradienteAritmetico(100, 0.1, 5), 3) == 686.180, "Error en presenteDadoGradienteAritmetico"
    assert round(anualidadDadoGradienteAritmetico(100, 0.1, 5), 3) == 181.013, "Error en anualidadDadoGradienteAritmetico"

    # Gradiente Geométrico (g != i)
    assert round(presenteDadoGradienteGeometrico(100, 0.05, 0.1, 5), 3) == 415.059, "Error en presenteDadoGradienteGeometrico (g ≠ i)"
    
    # Gradiente Geométrico (g = i)
    assert round(presenteDadoGradienteGeometrico(100, 0.1, 0.1, 5), 3) == 454.545, "Error en presenteDadoGradienteGeometrico (g = i)"
    
    print("¡Todos los tests pasaron exitosamente!")

# Ejecutar los tests
#test_formulas_financieras()