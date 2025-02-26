import inspect 
import customtkinter as ctk

from controller.gestorCalculos import escogerCalculo
from model.flujosEfectivo import *


def intercambiarFrames(frameParaMostrar, frameParaOcultar):
    frameParaMostrar.place(x=251, y=0)
    frameParaOcultar.place_forget()






conjuntoInputs = []
calculoSeleccionadoGlobal = ""

def mostrarInputsDadoSeleccion(self, calculoSeleccionado):

    global conjuntoInputs
    global calculoSeleccionadoGlobal

    for inputs in conjuntoInputs:
        inputs.destroy()
    conjuntoInputs.clear()

    calculoSeleccionadoGlobal = calculoSeleccionado
    firmaDeLaFuncion = inspect.signature(escogerCalculo(calculoSeleccionado))
    parametrosCalculoSeleccionado = list(firmaDeLaFuncion.parameters.keys())

    posicionVertical = 150

    for parametro in parametrosCalculoSeleccionado:
        
        placeholderInput = parametro

        inputParametro = ctk.CTkEntry(self, 
                                        width=350, 
                                        height=28, 
                                        font=("CTkFont", 15),
                                        placeholder_text=placeholderInput)
        inputParametro.place(x=455-175, y=posicionVertical)

        conjuntoInputs.append(inputParametro)

        posicionVertical += 45

    return conjuntoInputs


def llamarFuncionParaCalcular():

    param_1 = 0.0
    param_2 = 0.0
    param_3 = 0.0
    param_4 = 0.0

    valoresParametros = []
    for inputs in conjuntoInputs:
        valoresParametros.append(float(inputs.get()))

    if len(valoresParametros) > 3:
        param_1 = valoresParametros[0]
        param_2 = valoresParametros[1]
        param_3 = valoresParametros[2]
        param_4 = valoresParametros[3]
    else:
        param_1 = valoresParametros[0]
        param_2 = valoresParametros[1]
        param_3 = valoresParametros[2]


    if calculoSeleccionadoGlobal == "Futuro dado Presente":
        return futuroDadoPresente(param_1, param_2, param_3)
    
    elif calculoSeleccionadoGlobal == "Presente dado Futuro":
        return presenteDadoFuturo(param_1, param_2, param_3)
    
    elif calculoSeleccionadoGlobal == "Presente dado Anualidad":
        return presenteDadoAnualidad(param_1, param_2, param_3)
    
    elif calculoSeleccionadoGlobal == "Anualidad dado Presente":
        return anualidadDadoPresente(param_1, param_2, param_3)
    
    elif calculoSeleccionadoGlobal == "Futuro dado Anualidad":
        return futuroDadoAnualidad(param_1, param_2, param_3)
        
    elif calculoSeleccionadoGlobal == "Anualidad dado Futuro":
        return anualidadDadoFuturo(param_1, param_2, param_3)
    
    elif calculoSeleccionadoGlobal == "Presente dado Gradiente Aritmético":
        return presenteDadoGradienteAritmetico(param_1, param_2, param_3)
    
    elif calculoSeleccionadoGlobal == "Anualidad dado Gradiente Aritmético":
        return anualidadDadoGradienteAritmetico(param_1, param_2, param_3)
    
    elif calculoSeleccionadoGlobal == "Presente dado Gradiente Geométrico":
        return presenteDadoGradienteGeometrico(param_1, param_2, param_3, param_4)