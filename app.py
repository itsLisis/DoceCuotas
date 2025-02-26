import customtkinter as ctk

from view.interfazAlternativas import AlternativasFrame
from view.interfazFlujos import FlujosFrame
from config import * # Colores, constantes, etc

def main():


    ctk.set_default_color_theme("blue") 
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.geometry("1280x700")
    app.title("Doce Cuotas")


    # Tabview es como una especie de "lista" que va a contener las pestañas
    # como la barrita del navegador para añadir otra pestaña
    tabView = ctk.CTkTabview(app,
        fg_color = dark_gray_1, # Color del fondo del Widget
        segmented_button_fg_color = dark_gray_2, # Color del fondo del grupo de pestañas
        segmented_button_selected_color = dark_gray_1, # Colro de la pestaña seleccionada
        segmented_button_selected_hover_color = dark_gray_1, # Color de la pestaña seleccionada al pasar el mouse
        segmented_button_unselected_color = dark_gray_2,
        segmented_button_unselected_hover_color = dark_blue,
        anchor="nw",
        )
    tabView.pack(padx=3, pady=3, expand=True, fill="both")

    # con tabView.add estamos añadiendo una pestaña a nuestra lista o barrita
    flujosTab = tabView.add("Flujos de Caja")
    FlujosFrame(flujosTab)
    

    # lo mismo de arriba pero añadiendo otra pestaña
    alternativasTab = tabView.add("Elección de Alternativas")
    alternativas_frame = AlternativasFrame(alternativasTab)
    alternativas_frame.pack(expand=True, fill="both")


    app.mainloop()

if __name__ == "__main__":
    main()