from model.flujosEfectivo import *
from model.eleccionAlternativas import *
from controller.backGPT import *

def escogerCalculo(calculoSeleccionado):
    if calculoSeleccionado == "Futuro dado Presente":
        return futuroDadoPresente
    
    elif calculoSeleccionado == "Presente dado Futuro":
        return presenteDadoFuturo
    
    elif calculoSeleccionado == "Presente dado Anualidad":
        return presenteDadoAnualidad
    
    elif calculoSeleccionado == "Anualidad dado Presente":
        return anualidadDadoPresente
    
    elif calculoSeleccionado == "Futuro dado Anualidad":
        return futuroDadoAnualidad
        
    elif calculoSeleccionado == "Anualidad dado Futuro":
        return anualidadDadoFuturo
    
    elif calculoSeleccionado == "Presente dado Gradiente Aritmético":
        return presenteDadoGradienteAritmetico
    
    elif calculoSeleccionado == "Anualidad dado Gradiente Aritmético":
        return anualidadDadoGradienteAritmetico
    
    elif calculoSeleccionado == "Presente dado Gradiente Geométrico":
        return presenteDadoGradienteGeometrico
    



"""
    La funcion UsarInformacionEnviada es de ejemplo, la puede poner 
    en donde la necesite siempre y cuando la importe en interfazAlternativas.py
"""

# Indices de la informacion: 
# 0 = es tmar?
# 1 = rendimiento
# 2 = alternativa 1 [costo inicial, operacion anual, valor rescate, vida util]
# 3 = alternativa 2 [costo inicial, operacion anual, valor rescate, vida util]
# 4 = prompt gpt

def usarInformacionEnviada(listaConTodaLaInformacion) -> str:
    seleccion: bool = False
    resultadosRC: list = []
    interesAproximado: list = []

    promptDeUsuario: str = "Información de las alternativas:\n"

    promptDeUsuario += "- Alternativa Uno:\n"
    promptDeUsuario += f" - Costo inicial (inversión): {listaConTodaLaInformacion[2][0]}\n"
    promptDeUsuario += f" - Costo de operación anual: {listaConTodaLaInformacion[2][1]}\n"
    promptDeUsuario += f" - Valor de rescate: {listaConTodaLaInformacion[2][2]}\n"
    promptDeUsuario += f" - Vida útil: {listaConTodaLaInformacion[2][3]}\n\n"

    promptDeUsuario += "- Alternativa Dos:\n"
    promptDeUsuario += f" - Costo inicial (inversión): {listaConTodaLaInformacion[3][0]}\n"
    promptDeUsuario += f" - Costo de operación anual: {listaConTodaLaInformacion[3][1]}\n"
    promptDeUsuario += f" - Valor de rescate: {listaConTodaLaInformacion[3][2]}\n"
    promptDeUsuario += f" - Vida útil: {listaConTodaLaInformacion[3][3]}\n\n"

    promptDeUsuario += "Se seleccionó el método "

    if (listaConTodaLaInformacion[0]):
        seleccion = alternativaPorTabla(
            listaConTodaLaInformacion[1],
            listaConTodaLaInformacion[2],
            listaConTodaLaInformacion[3],
            interesAproximado
            )
        promptDeUsuario += "Análisis de Tasa de Rendimiento (Método Tabular).\n\n"
        promptDeUsuario += f"Datos:\n- Valor de la TMAR: {listaConTodaLaInformacion[1]}\n"
        promptDeUsuario += f"- Interés hallado de manera aproximada.: {interesAproximado[0]}\n\n"
    else:
        seleccion = alternativaPorRC(
            listaConTodaLaInformacion[1],
            listaConTodaLaInformacion[2],
            listaConTodaLaInformacion[3],
            resultadosRC
            )
        promptDeUsuario += "Método del Valor Anual (VA).\n\n"
        promptDeUsuario += f"Datos:\n- Interés: {listaConTodaLaInformacion[1]}\n"
        promptDeUsuario += f"- Valor anual alternativa Uno: {resultadosRC[0]}\n"
        promptDeUsuario += f"- Valor anual alternativa Dos: {resultadosRC[1]}\n\n"

    promptDeUsuario += f"La alternativa seleccionada según cálculos:\nAlternativa Uno: {seleccion}\n\n\n"

    promptDeUsuario += f"Mi petición:\n\n {listaConTodaLaInformacion[4]}"

    with open("prompt.txt", "r", encoding="utf-8") as file:
        promptDeDesarrollo = file.read().strip()

    # respuesta: str = obtenerRespuesta(promptDeDesarrollo, promptDeUsuario)
    respuesta: str = "uwu"

    print(promptDeDesarrollo)
    print(promptDeUsuario)

    return respuesta
