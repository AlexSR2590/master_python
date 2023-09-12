# Menus con tkinter
from tkinter import *

window = Tk()
window.title("Menus")
window.geometry("500x300")

# Creando menu
mi_menu = Menu(window)
window.config(menu=mi_menu)

submenu_archivo = Menu(mi_menu, tearoff=0)
submenu_archivo.add_command(label="Nuevo archivo de texto")
submenu_archivo.add_command(label="Nuevo archivo")
submenu_archivo.add_command(label="Nueva ventana")
submenu_archivo.add_separator()
submenu_archivo.add_command(label="Salir", command=window.quit)

mi_menu.add_cascade(label="Archivo", menu=submenu_archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Selección")

window.mainloop()