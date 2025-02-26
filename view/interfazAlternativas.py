import customtkinter as ctk
from config import *

#from view.interfazAlternativaUno import alternativaUnoFrame



# aqui podriamos poner simplemente las funciones sin mas, pero al crear una clase Frame
# podemos ser mas modulares y robustos
class AlternativasFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(pady=(3,0),expand=True, fill="both")
        self.configure(fg_color=dark_gray_2)

    # aqui creamos todas las cosas visuales o Widgets que queremos
    def create_widgets(self):

        # Frame para Alternativa Uno
        frameAlternativaUno = ctk.CTkFrame(master=self, width=610, height=240, fg_color=dark_gray_3)
        frameAlternativaUno.place(x=15, y=40)
        # Label para Alternativa Uno
        labelAlternativaUno = ctk.CTkLabel(self, text="Alternativa Uno",font=("CTkFont", 18), fg_color="transparent")
        labelAlternativaUno.place(x=25, y=11)

        # Frame para Alternaitva Dos
        frameAlternativaDos = ctk.CTkFrame(master=self, width=610, height=240, fg_color=dark_gray_3)
        frameAlternativaDos.place(x=15, y=315)
        # Label para Alternativa Dos
        labelAlternativaUno = ctk.CTkLabel(self, text="Alternativa Dos",font=("CTkFont", 18), fg_color="transparent")
        labelAlternativaUno.place(x=25, y=285)


        # Slider Interes
        def seleccionarInteres(valorInteres):
            print(f"Interes Slider: {valorInteres}")
            labelInteres.configure(text=round(valorInteres,2))
        
        sliderInteres = ctk.CTkSlider(self, from_=0, to=100, 
                                      width = 610,
                                      height = 18,
                                      progress_color = dark_blue,
                                      command = seleccionarInteres)
        
        sliderInteres.place(x=15, y=585)

        labelInteres = ctk.CTkLabel(self, 
                                    fg_color="transparent",
                                    text="Selecciona el Interés",
                                    font=("CTkFont", 18),
                                    width=50,
                                    height=20)
        labelInteres.place(x=22, y=565)


        # Boton añadir flujo por periodo para la alternativaUno
        botonAñadirFlujoAlternativaUno = ctk.CTkButton(self, 
                                                    text="+", 
                                                    fg_color=dark_blue,
                                                    font=("CTkFont", 20),
                                                    width = 40,
                                                    height = 40,
                                                    command=lambda: print("Flujo AlternativaUno Añadido"))
        botonAñadirFlujoAlternativaUno.place(x = 575, y = 230)


        # Boton añadir flujo por periodo
        botonAñadirFlujoAlternativaDos = ctk.CTkButton(self, 
                                                    text="+", 
                                                    fg_color=dark_blue,
                                                    font=("CTkFont", 20),
                                                    width = 40,
                                                    height = 40,
                                                    command=lambda: print("Flujo AlternativaDos Añadido"))
        botonAñadirFlujoAlternativaDos.place(x = 575, y = 505)
        

        # Frame para el Prompt 
        framePrompt = ctk.CTkFrame(master=self, width=610, height=130, fg_color=dark_gray_3)
        framePrompt.place(x=637, y=40)
        # Label para el Prompt
        labelPrompt = ctk.CTkLabel(self, text="Prompt",font=("CTkFont", 18), fg_color="transparent")
        labelPrompt.place(x=647, y=11)


        # Frame para la respuesta del Prompt 
        frameRespuesta = ctk.CTkFrame(master=self, width=610, height=350, fg_color=dark_gray_3)
        frameRespuesta.place(x=637, y=250)
        # Label para el framePrompt
        labelRespuesta = ctk.CTkLabel(self, text="Análisis",font=("CTkFont", 18), fg_color="transparent")
        labelRespuesta.place(x=647, y=220)

        # Boton para enviar los datos y el prompt
        botonEnviarPrompt = ctk.CTkButton(self, 
                                                    text="Enviar datos y analizar", 
                                                    fg_color=dark_blue,
                                                    font=("CTkFont", 15),
                                                    width = 200,
                                                    height = 28,
                                                    command=lambda: print("Prompt Enviado"))
        botonEnviarPrompt.place(x = 1043, y = 180)



        #alternativaUnoFrame(frameAlternativaUno)
    # aqui le damos funcionalidad a esow Widgets, usando el controlador
    # para que traiga las funciones de calculos

