import inspect 
import customtkinter as ctk

from controller.gestorCalculos import escogerCalculo


def intercambiarFrames(frameParaMostrar, frameParaOcultar):
    frameParaMostrar.place(x=251, y=0)
    frameParaOcultar.place_forget()






entradas = []
def mostrarInputsDadoSeleccion(self, calculoSeleccionado):

    global entradas

    for entrada in entradas:
        entrada.destroy()
    entradas.clear()

    
    firmaDeLaFuncion = inspect.signature(escogerCalculo(calculoSeleccionado))
    parametrosCalculoSeleccionado = list(firmaDeLaFuncion.parameters.keys())

    posicionVertical = 150
    print("Cálculo seleccionado:", calculoSeleccionado)

    
    for parametro in parametrosCalculoSeleccionado:
        
        placeholderInput = parametro

        inputParametro = ctk.CTkEntry(self, 
                                        width=350, 
                                        height=28, 
                                        font=("CTkFont", 15),
                                        placeholder_text=placeholderInput)
        inputParametro.place(x=455-175, y=posicionVertical)


        entradas.append(inputParametro)

        posicionVertical += 45