import customtkinter as ctk
from config import *

# aqui podriamos poner simplemente las funciones sin mas, pero al crear una clase Frame
# podemos ser mas modulares y robustos
class AlternativasFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(pady=(3,0),expand=True, fill="both")
        self.configure(fg_color=dark_gray_2)

        self.periodosAlternativaUno = 0
        self.posVerticalAlternativaUnoPar = 50
        self.posVerticalAlternativaUnoImpar = 50
        
        self.periodosAlternativaDos = 0
        self.posVerticalAlternativaDosPar = 325
        self.posVerticalAlternativaDosImpar = 325

    # aqui creamos todas las cosas visuales o Widgets que queremos
    def create_widgets(self):
        
        # Esta es una funcion un poco XDDDD, definitivamente no cumple la Unica Responsabilidad pero bue
        entrysAlternativaUno = []
        def crearEntryAlternativaUno(self, periodosAlternativaUno, 
                                     posVerticalAlternativaUnoPar,
                                     posVerticalAlternativaUnoImpar):
            
            if periodosAlternativaUno%2 == 0:
                inputAlternativaUno = ctk.CTkEntry(self, 
                                            width=250, 
                                            height=28, 
                                            font=("CTkFont", 15),
                                            placeholder_text=f"Periodo {periodosAlternativaUno}")
                inputAlternativaUno.place(x=25, y=posVerticalAlternativaUnoPar)
                self.posVerticalAlternativaUnoPar += 38

            else:
                inputAlternativaUno = ctk.CTkEntry(self, 
                                            width=250, 
                                            height=28, 
                                            font=("CTkFont", 15),
                                            placeholder_text=f"Periodo {periodosAlternativaUno}")
                inputAlternativaUno.place(x=285, y=posVerticalAlternativaUnoImpar)
                self.posVerticalAlternativaUnoImpar += 38

            entrysAlternativaUno.append(inputAlternativaUno)
            self.periodosAlternativaUno += 1
        
        # Obtener en una lista los valores de los inputs para la alternativaUno
        valoresAlternativaUno = []
        def obtenerValoresAlternativaUno():
            for entry in entrysAlternativaUno:
                valoresAlternativaUno.append(entry.get())

            print(valoresAlternativaUno)

        # Eliminar ultimo flujo agregado a la alternativaUNo
        def eliminarUltimoFlujoAlternativaUno(self, 
                                              periodosAlternativaUno,
                                              posVerticalAlternativaUnoPar,
                                              posVerticalAlternativaUnoImpar
                                              ):
            
            if periodosAlternativaUno%2 == 0:
                if periodosAlternativaUno >= 1:
                    self.posVerticalAlternativaUnoImpar -= 38
            else:
                if periodosAlternativaUno >= 1:
                    self.posVerticalAlternativaUnoPar -= 38
            
            if periodosAlternativaUno > 0:
                self.periodosAlternativaUno -= 1
            else:
                self.periodosAlternativaUno = 0

            entrysAlternativaUno[-1].place_forget()
            entrysAlternativaUno.pop()


        entrysAlternativaDos = []
        def crearEntryAlternativaDos(self, periodosAlternativaDos, 
                                     posVerticalAlternativaDosPar,
                                     posVerticalAlternativaDosImpar):
            
            if periodosAlternativaDos%2 == 0:
                inputAlternativaDos = ctk.CTkEntry(self, 
                                            width=250, 
                                            height=28, 
                                            font=("CTkFont", 15),
                                            placeholder_text=f"Periodo {periodosAlternativaDos}")
                inputAlternativaDos.place(x=25, y=posVerticalAlternativaDosPar)
                self.posVerticalAlternativaDosPar += 38

            else:
                inputAlternativaDos = ctk.CTkEntry(self, 
                                            width=250, 
                                            height=28, 
                                            font=("CTkFont", 15),
                                            placeholder_text=f"Periodo {periodosAlternativaDos}")
                inputAlternativaDos.place(x=285, y=posVerticalAlternativaDosImpar)
                self.posVerticalAlternativaDosImpar += 38

            entrysAlternativaDos.append(inputAlternativaDos)
            self.periodosAlternativaDos += 1
        
        # Obtener en una lista los valores de los inputs para la alternativaUno
        valoresAlternativaDos = []
        def obtenerValoresAlternativaDos():
            for entry in entrysAlternativaDos:
                valoresAlternativaDos.append(entry.get())

            print(valoresAlternativaDos)

        # Eliminar ultimo flujo agregado a la alternativaUNo
        def eliminarUltimoFlujoAlternativaDos(self, 
                                              periodosAlternativaDos,
                                              posVerticalAlternativaDosPar,
                                              posVerticalAlternativaDosImpar
                                              ):
            
            if periodosAlternativaDos%2 == 0:
                if periodosAlternativaDos >= 1:
                    self.posVerticalAlternativaDosImpar -= 38
            else:
                if periodosAlternativaDos >= 1:
                    self.posVerticalAlternativaDosPar -= 38
            
            if periodosAlternativaDos > 0:
                self.periodosAlternativaDos -= 1
            else:
                self.periodosAlternativaDos = 0

            entrysAlternativaDos[-1].place_forget()
            entrysAlternativaDos.pop()

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
            labelInteres.configure(text=f"Interés: {round(valorInteres,2)}")
        
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
                                                    text="➕", 
                                                    fg_color=dark_blue,
                                                    font=("CTkFont", 12),
                                                    width = 40,
                                                    height = 40,
                                                    command=lambda: crearEntryAlternativaUno(self, 
                                                                        self.periodosAlternativaUno, 
                                                                        self.posVerticalAlternativaUnoPar,
                                                                        self.posVerticalAlternativaUnoImpar
                                                                        )
                                                    )
        botonAñadirFlujoAlternativaUno.place(x = 575, y = 230)

        # Boton eliminar ultimo flujo para la alternativaUno
        botonEliminarFlujoAlternativaUno = ctk.CTkButton(self, 
                                                    text="➖", 
                                                    fg_color=dark_blue,
                                                    font=("CTkFont", 12),
                                                    width = 40,
                                                    height = 40,
                                                    command=lambda:eliminarUltimoFlujoAlternativaUno(self, 
                                                                        self.periodosAlternativaUno, 
                                                                        self.posVerticalAlternativaUnoPar,
                                                                        self.posVerticalAlternativaUnoImpar
                                                                        ))                     
        botonEliminarFlujoAlternativaUno.place(x = 575, y = 185)


        # Boton añadir flujo por periodo
        botonAñadirFlujoAlternativaDos = ctk.CTkButton(self, 
                                                    text="➕", 
                                                    fg_color=dark_blue,
                                                    font=("CTkFont", 12),
                                                    width = 40,
                                                    height = 40,
                                                    command=lambda: crearEntryAlternativaDos(self,
                                                                        self.periodosAlternativaDos,
                                                                        self.posVerticalAlternativaDosPar,
                                                                        self.posVerticalAlternativaDosImpar))
        botonAñadirFlujoAlternativaDos.place(x = 575, y = 505)
        
        # Boton eliminar ultimo flujo para la alternativaDos
        botonEliminarFlujoAlternativaDos = ctk.CTkButton(self, 
                                                    text="➖", 
                                                    fg_color=dark_blue,
                                                    font=("CTkFont", 12),
                                                    width = 40,
                                                    height = 40,
                                                    command=lambda:eliminarUltimoFlujoAlternativaDos(self, 
                                                                        self.periodosAlternativaDos, 
                                                                        self.posVerticalAlternativaDosPar,
                                                                        self.posVerticalAlternativaDosImpar
                                                                        ))    
        botonEliminarFlujoAlternativaDos.place(x = 575, y = 460)
        
        
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
                                                    command=lambda: obtenerValoresAlternativaUno())
        botonEnviarPrompt.place(x = 1043, y = 180)



    #alternativaUnoFrame(frameAlternativaUno)
    # aqui le damos funcionalidad a esow Widgets, usando el controlador
    # para que traiga las funciones de calculos