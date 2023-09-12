from tkinter import *
import os.path
from PIL import Image, ImageTk

window = Tk()
window.geometry("700x500")
Label(window, text="Hola soy Alexis").pack(anchor=W)
window.title("Imagenes con tkinter")
icon = "./imagenes/imagenes.ico"
icon_alt="./21-tkinter/imagenes/imagenes.ico"

path_image = "./imagenes/luna.png"
imagen = Image.open(path_image)

render_image = ImageTk.PhotoImage(imagen)
Label(window, image= render_image).pack(anchor=E)

# Guardar la ruta absoluta (la imagen folder.ico )
path_icono = os.path.abspath(icon)
# Comprobar si el archivo existe
if not os.path.isfile(path_icono):
# Guardar la ruta absoluta (la imagen folder.ico )
    path_icono = os.path.abspath(icon_alt)
window.iconbitmap(path_icono)

window.mainloop()