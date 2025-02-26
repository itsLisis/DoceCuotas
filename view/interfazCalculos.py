import customtkinter as ctk
from config import *

class FlujosCalculosFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.configure(fg_color=light_gray_3, width=910, height=350)
        self.place(x=506-455, y=50)

    def create_widgets(self):
        labelTitulo = ctk.CTkLabel(self, text="¿Qué deseas calcular?",font=("CTkFont", 18), fg_color=light_gray_3)
        labelTitulo.place(x=360, y=35)

        #botonGraficar = ctk.CTkButton(self, text="Calcular", font=("CTkFont", 15),
                                    #command=lambda:print("Calcular"))
        #botonGraficar.place(x=30, y=120)

        opciones = [
            "Futuro dado Presente                                                                                                                        ",
            "Presente dado Futuro",
            "Presente dado Anualidad",
            "Anualidad dado Presente",
            "Futuro dado Anualidad",
            "Anualidad dado Futuro",
            "Presente dado Gradiente Aritmético",
            "Anualidad dado Gradiente Aritmético",
            "Presente dado Gradiente Geométrico",  
        ]




        menuOpciones = ctk.CTkOptionMenu(self, values=opciones,
                                        width=700,
                                        height=28,
                                        font=("CTkFont", 15),
                                        dropdown_font=("CTkFont", 15),
                                        dropdown_fg_color=light_gray_3,
                                        dropdown_hover_color=dark_blue,
                                        )
        menuOpciones.place(x=455-350, y=90)

