from tkinter import *
from tkinter import messagebox as MessageBox
window = Tk()

window.title("Alertas")
window.geometry("700x500")
window.config(bd=70)
def mostrarAlerta():
    MessageBox.showinfo("Alerta", "Mensaje desde función mostrarAlerta")

def salir(name):
    resultado = MessageBox.askquestion("Salir", "¿Continujar ejecutando la aplicación?")
    if  resultado != "yes":
        MessageBox.showinfo("Adios", f"Hasta pronto {name}")
        window.destroy()

name = "Alexis Arturo"
Button(window, text="Mostar alerta", command=mostrarAlerta).pack()

Button(window, text="Salir", command= lambda: salir(name)).pack()
window.mainloop()