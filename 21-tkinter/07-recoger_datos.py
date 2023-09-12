from tkinter import *
window = Tk()
window.title("Recoger datos de formulario")
window.geometry("700x600")
window.config(bd=30)

def getDato():
    resultado.set(dato.get())
    if len(resultado.get()) >= 1:
        texto_recogido.config(bg="black", fg="white")




dato = StringVar()
resultado = StringVar()

Label(window, text="Introduce un texto: ").pack(anchor=NW)
Entry(window, textvariable=dato).pack(anchor=NW)

Label(window, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(window, textvariable=resultado)
texto_recogido.pack(anchor=NW)
Button(window, text="Mostrar dato", command=getDato).pack(anchor=NW)

window.mainloop()