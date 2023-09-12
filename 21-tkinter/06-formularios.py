from tkinter import *

window = Tk()
window.title("Formularios con Tkinter") 
window.geometry("700x400")

# Texto encabezado
header = Label(window, text="Formularios con Tkinter")
header.config(
    fg="white",
    bg="darkgray",
    font= ("Open Sans",18),
    padx=10,
    pady=5
)
header.grid(row=0, column=0, columnspan=12, sticky=NW)

# Label para el campo nombre
name = Label(window, text="Nombre:")
name.grid(column=0, row=1, sticky=W, padx=5, pady=5)
# Campo de texto nombre
name_box = Entry(window)
name_box.grid(column=1, row=1, sticky=W, padx=5, pady=5) 
name_box.config(justify="right", state="normal")

# Label apellidos
last_name = Label(window, text="Apellidos: ")
last_name.grid(column=0, row=2, sticky=W, padx=5, pady=5)
# Campo texto apellidos
last_name_box = Entry(window)
last_name_box.grid(column=1, row=2, sticky=W, padx=5, pady=5)
last_name_box.config(justify="left", state="normal")

# Label campo de texto para descripción
description = Label(window, text="Descripción: ")
description.grid(column=0, row=3, sticky=N, padx=5, pady=5)
# Campo de texto grande para la descripción
description_box = Text(window)
description_box.grid(column=1, row=3)
description_box.config(width=30, height=5, font=("Arial", 12), padx=15, pady=15)

# Creando un boton 
boton = Button(window, text="Enviar")
boton.grid(column=1, row=4, sticky=E, padx=10, pady=10)
boton.config(bg="black", fg="white")


window.mainloop()