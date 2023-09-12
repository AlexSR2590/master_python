from tkinter import *
window = Tk()
window.geometry("500x500")

def pruebas(name, last_name):
    return f"Hola {name} {last_name}, bienvenido"


texto = Label(window, text="Bienvenido a mi programa" )
texto.config(
    fg="white", 
    bg="black", 
    padx=50, 
    pady=20,
    font=("Arial", 30)
    )
texto.pack()

texto = Label(window, text= pruebas(last_name="Alexis Arturo", name="Solis Rodriguez"))
texto.config(
    height=3,
    bg="orange",
    fg="white",
    font=("Arial", 18), 
    padx=10,
    pady=20,
    cursor="spider"
    )
texto.pack(anchor=SE)

texto = Label(window, text="Master en Python")
texto.config(
    height=3,
    bg="red",
    fg="white",
    font=("Arial", 18), 
    padx=10,
    pady=20,
    cursor="circle"
    )
texto.pack(anchor=NW)

window.mainloop()