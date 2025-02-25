import customtkinter as ctk
from config import *
from controller.gestorFrames import intercambiarFrames

# aqui podriamos poner simplemente las funciones sin mas, pero al crear una clase Frame
# podemos ser mas modulares y robustos
class FlujosFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(pady=(3,0),expand=True, fill="both")
        self.configure(fg_color=dark_gray_1)

    # aqui creamos todas las cosas visuales o Widgets que queremos
    def create_widgets(self):

        frameMenu = ctk.CTkFrame(master=self, width=242, height=643, fg_color=dark_gray_2)
        frameMenu.place(x=0, y=0)

        frameGraficos = ctk.CTkFrame(master=self, width=1012, height=643, fg_color="red")
        frameGraficos.place(x=251, y=0)

        frameCalculos = ctk.CTkFrame(master=self, width=1012, height=643, fg_color=dark_gray_2)
        frameCalculos.place(x=251, y=0)

        labelTitulo = ctk.CTkLabel(self, text="Cálculos de Flujos",font=("CTkFont", 18), fg_color=dark_gray_2)
        labelTitulo.place(x=45, y=50)



        botonCalcular = ctk.CTkButton(self, text="Calcular", font=("CTkFont", 15),
                                    command=lambda:intercambiarFrames(frameCalculos, frameGraficos))
        botonCalcular._hover_color = dark_blue
        botonCalcular._fg_color = light_gray
        botonCalcular.place(x=50, y=90)

        botonGraficar = ctk.CTkButton(self, text="Graficar", font=("CTkFont", 15),
                                    command=lambda:intercambiarFrames(frameGraficos, frameCalculos))
        botonGraficar._hover_color = dark_blue
        botonGraficar._fg_color = light_gray
        botonGraficar.place(x=50, y=130)