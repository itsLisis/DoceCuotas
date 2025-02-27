import customtkinter as ctk
from config import *


"""
    Este es el import de la funcion que usted cree
"""
from controller.gestorCalculos import usarInformacionEnviada 


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


        listaConTodaLaInformacion = []
        def obtenerValoresParaEnviar():
            
            boolTMAR = obtenerBoolTMAR()
        
            infoPrompt = textBoxPrompt.get("1.0", "end-1c")
            valorInteres = sliderInteres.get()
            valoresInputsAlternativaUno = []
            valoresInputsAlternativaDos = []
            
            for input in inputsAlternativaUno:
                valoresInputsAlternativaUno.append(float(int(input.get())))

            for input in inputsAlternativaDos:
                valoresInputsAlternativaDos.append(float(int(input.get())))
            
            listaConTodaLaInformacion.extend([boolTMAR, valorInteres,valoresInputsAlternativaUno, valoresInputsAlternativaDos, infoPrompt])


            """
                Para mi queridisimo Omar:

                usarInformacionEnviada es la funcion que importamos desde
                gestorCalculos.py en la carpeta controller.
                Recibe como parametro la lista listaConTodaLaInformacion
            """
            usarInformacionEnviada(listaConTodaLaInformacion)
        
        

        # Frame para Alternativa Uno
        frameAlternativaUno = ctk.CTkFrame(master=self, width=570, height=240, fg_color=light_gray_3)
        frameAlternativaUno.place(x=15, y=40)
        # Label para Alternativa Uno
        labelAlternativaUno = ctk.CTkLabel(self, text="Alternativa Uno",font=("CTkFont", 18), fg_color="transparent")
        labelAlternativaUno.place(x=25, y=11)

        # Frame para Alternaitva Dos
        frameAlternativaDos = ctk.CTkFrame(master=self, width=570, height=240, fg_color=light_gray_3)
        frameAlternativaDos.place(x=15, y=315)
        # Label para Alternativa Dos
        labelAlternativaUno = ctk.CTkLabel(self, text="Alternativa Dos",font=("CTkFont", 18), fg_color="transparent")
        labelAlternativaUno.place(x=25, y=285)



        listaTextoAlternativas = ["Costo Inicial", "Costo Operación Anual",
                                "Valor de Rescate", "Vida Útil"]
        

        # Inputs y Labels para Alternativa Uno
        posicionVerticalLabelAlternativaUno = 45
        posicionVerticalInputAlternativaUno = 70
        
        inputsAlternativaUno = []
        for elemento in listaTextoAlternativas:

            labelAlternativaUno = ctk.CTkLabel(self, text=elemento,
                                                font=("CTkFont", 15), fg_color=light_gray_3)
            labelAlternativaUno.place(x=45, y=posicionVerticalLabelAlternativaUno)

            inputAlternativaUno = ctk.CTkEntry(self, 
                                        width=480, 
                                        height=28, 
                                        font=("CTkFont", 13),
                                        placeholder_text= "0")
            inputAlternativaUno.place(x=35, y=posicionVerticalInputAlternativaUno)
                                            #x=35
            inputsAlternativaUno.append(inputAlternativaUno)

            posicionVerticalLabelAlternativaUno += 55
            posicionVerticalInputAlternativaUno += 55


        # Inputs y Labels para Alternativa Dos

        posicionVerticalLabelAlternativaDos = 322
        posicionVerticalInputAlternativaDos = 347

        inputsAlternativaDos = []
        for elemento in listaTextoAlternativas:

            labelAlternativaDos = ctk.CTkLabel(self, text=elemento,
                                                font=("CTkFont", 15), fg_color=light_gray_3)
            labelAlternativaDos.place(x=45, y=posicionVerticalLabelAlternativaDos)

            inputAlternativaDos = ctk.CTkEntry(self, 
                                        width=480, 
                                        height=28, 
                                        font=("CTkFont", 13),
                                        placeholder_text= "0")
            inputAlternativaDos.place(x=35, y=posicionVerticalInputAlternativaDos)

            inputsAlternativaDos.append(inputAlternativaDos)

            posicionVerticalLabelAlternativaDos += 55
            posicionVerticalInputAlternativaDos += 55
        

        # Slider Interes
        def seleccionarInteres(valorInteres):
            labelInteres.configure(text=f"Rendimiento: {round(valorInteres,2)}%")
        
        sliderInteres = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=200,
                                    fg_color = light_gray_3,
                                    width = 450,
                                    height = 18,
                                    progress_color = dark_blue,
                                    command = seleccionarInteres)
        
        sliderInteres.place(x=15, y=605)

        labelInteres = ctk.CTkLabel(self, 
                                    fg_color="transparent",
                                    text="Selecciona el Rendimiento",
                                    font=("CTkFont", 18),
                                    width=50,
                                    height=20)
        labelInteres.place(x=22, y=575)
        
        

        def obtenerBoolTMAR():

            boolTMAR = switchTMAR.get()

            if boolTMAR == 1:
                boolTMAR = True
                labelTMAR.configure(text="TMAR: Si")
            else:
                boolTMAR = False
                labelTMAR.configure(text="TMAR: No")
            
            return boolTMAR
        
        labelTMAR = ctk.CTkLabel(self, 
                                    fg_color="transparent",
                                    text="TMAR: No",
                                    font=("CTkFont", 18),
                                    width=50,
                                    height=20)
        labelTMAR.place(x=495,y=575)
        switchTMAR = ctk.CTkSwitch(self, width=40, height=28,
                                    switch_width=45, switch_height=25, text="",
                                    command=lambda:obtenerBoolTMAR())
        switchTMAR.place(x=495,y=600)


        # Frame para el Prompt 
        framePrompt = ctk.CTkFrame(master=self, width=645, height=130, fg_color=light_gray_3)
        framePrompt.place(x=600, y=40)
        # Label para el Prompt
        labelPrompt = ctk.CTkLabel(self, text="Prompt",font=("CTkFont", 18), fg_color="transparent")
        labelPrompt.place(x=610, y=11)

        # Textbox para el Prompt
        textBoxPrompt = ctk.CTkTextbox(self, width=630, height=120,
                                        font=("CTkFont", 15),
                                        fg_color=light_gray_3,
                                        corner_radius=0
                                        )
        textBoxPrompt.place(x=609, y=45)

        # Frame para la respuesta del Prompt 
        frameRespuesta = ctk.CTkFrame(master=self, width=645, height=370, fg_color=light_gray_3)
        frameRespuesta.place(x=600, y=250)
        # Label para el framePrompt
        labelRespuesta = ctk.CTkLabel(self, text="Análisis",font=("CTkFont", 18), fg_color="transparent")
        labelRespuesta.place(x=610, y=220)


        # Textbox para la Respuesta
        textBoxRespuesta = ctk.CTkTextbox(self, width=630, height=352,
                                        fg_color=light_gray_3,
                                        font=("CTkFont", 15),
                                        corner_radius=0,
                                        state="disable"
                                        )
        textBoxRespuesta.place(x=609, y=260)

        # Boton para enviar los datos y el prompt
        botonEnviarPrompt = ctk.CTkButton(self, 
                                                    text="Enviar datos y analizar", 
                                                    fg_color=dark_blue,
                                                    font=("CTkFont", 15),
                                                    width = 200,
                                                    height = 28,
                                                    command=lambda: obtenerValoresParaEnviar())
        botonEnviarPrompt.place(x = 1043, y = 180)






        """
        En la funcion actualizarTextoConRespuesta simplemente hay que pasarle el texto plano
        con la respuesta de ChatGPT (importada desde donde sumercé haga la lógica del back".
        """
                                        # Texto plano con respuesta del chatGPT
        def actualizarTextoConRespuesta(texto):
            textBoxRespuesta.configure(state="normal")

            textBoxRespuesta.insert("1.0", "XD"*500) # eliminar o comentar esta linea
            """#textBoxRespuesta.insert("1.0", AQUI VA EL PARAMETRO {texto})"""

            textBoxRespuesta.configure(state="disable")