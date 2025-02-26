from model.flujosEfectivo import *

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