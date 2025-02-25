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

    # aqui creamos todas las cosas visuales o Widgets que queremos
    def create_widgets(self):
        label = ctk.CTkLabel(self, text="Cálculos de Alternativas")
        label.pack(pady=10)

        button = ctk.CTkButton(self, text="Calcular", command=self.calcular)
        button.pack(pady=10)

    # aqui le damos funcionalidad a esow Widgets, usando el controlador
    # para que traiga las funciones de calculos
    def calcular(self):
        print("Realizando cálculos de alternativas...")
