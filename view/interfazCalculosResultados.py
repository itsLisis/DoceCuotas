import customtkinter as ctk

from config import *

from view.interfazCalculos import resultadoCalculo

class FlujosResultadosFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.configure(fg_color=light_gray_3, width=910, height=100)
        self.place(x=506-455, y=495)

    def create_widgets(self):
        
        
        self.mostrarResultado = ctk.CTkLabel(master=self, 
                                        font = ("CTkFont", 45),
                                        fg_color="transparent",
                                        text=resultadoCalculo,
                                        anchor="center")

        self.mostrarResultado.place(relx=0.5, y=25)
        self.actualizarResultado()

    def actualizarResultado(self):
        from view.interfazCalculos import resultadoCalculo
        self.mostrarResultado.configure(text=str(resultadoCalculo))

        self.mostrarResultado.place(relx=0.5, y=50, anchor="center")

        self.after(200, self.actualizarResultado)