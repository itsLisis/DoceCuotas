# Aqui se pondran las funciones que no esten conectadas a la logica del negocio,
# sino que irán funciones alternas, como por ejemplos controlar la interfaz grafica


def intercambiarFrames(frameParaMostrar, frameParaOcultar):
    frameParaMostrar.place(x=251, y=0)
    frameParaOcultar.place_forget()

