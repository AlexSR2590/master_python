# Tkinter es un modulo para crear interfaces graficas de usuario
from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "Interfaz gráfica con Python y Tkinter"
        self.icon = "./imagenes/folder.ico"
        self.icon_alt = "./21-tkinter/imagenes/folder.ico"
        self.size = "770x470"
        self.resizable = False
        

    def cagarVentana(self):
        #Crear la ventana principal
        window = Tk()
        self.window = window
        # Título de la ventana
        window.title(self.title)

        # Guardar la ruta absoluta (la imagen folder.ico )
        path_icono = os.path.abspath(self.icon)

        # Comprobar si el archivo existe
        if not os.path.isfile(path_icono):
            # Guardar la ruta absoluta (la imagen folder.ico )
            path_icono = os.path.abspath(self.icon_alt)


        # cargar icono de la ventana
        window.iconbitmap(path_icono)

        # Mostrar texto en la ventana del programa (se muestra la ruta del icono en la ventana)
        show_text = Label(window, text = path_icono)
        show_text.pack()

        # Cambiar el tamaño de la ventana
        window.geometry(self.size)

        if self.resizable:
            #Bloquear el tamaño de la venta
            window.resizable(1, 1)
        else:
            window.resizable(0, 0)
    
    def addTexto(self, message):
        texto = Label(self.window, text=message)
        texto.pack()

    # Metodo para inicar y mostrar la ventana hasta que se cierre
    def showProgram(self):
        self.window.mainloop()

# Instanciar obejo programa
program = Programa()
program.cagarVentana()
texto = "Hola desde un metodo"
program.addTexto(texto)
program.showProgram()

