from tkinter import *
window = Tk()
window.title("Formularios 2")
window.geometry("700x500")
header = Label(window, text="Formularios 2")
header.config(padx=15, pady=15, fg="white", bg="black", font=("Consolas", 20))
header.grid(column=0,row=0, columnspan=5, sticky=N)

# Botones check

def showProfesion():
    result = ""
    if web.get():
        result += "Soy desarrollador web "
        mostrar.config(text=result)
    if movil.get():
        result += "Soy desarrollador movil "
        mostrar.config(text=result)
    if consola.get():
        result += "Soy programador de consola "
    mostrar.config(
        text=result,
        bg="black", 
        fg="green"
    )

web = IntVar()
movil = IntVar()
consola = IntVar()
Label(window, text="¿A que te dedicas?").grid(column=0, row=1, sticky=W)
Checkbutton(
    window, 
    text="Desarrollo web", 
    variable=web, 
    onvalue=1, 
    offvalue=0,
    command=showProfesion).grid(column=0, row=2, sticky=W)
Checkbutton(
    window, 
    text="Desarrollo movil", 
    variable=movil, 
    onvalue=1, 
    offvalue=0, 
    command=showProfesion).grid(column=0, row=3, sticky=W)
Checkbutton(
    window, 
    text="Desarrollo consola", 
    variable=consola, 
    onvalue=1, 
    offvalue=0, 
    command=showProfesion).grid(column=0, row=4, sticky=W)
mostrar = Label(window)
mostrar.grid(column=0, row=5)

# Radio buttons

def marcar():
    marcado.config(text=option.get(), bg="black", fg="red")

option = StringVar()
option.set(None)
Label(window, text="¿Que sexo eres?").grid(column=0, row=6, sticky=W)
Radiobutton(
    window, 
    text="Masculino",
    value="Masculino",
    variable=option,
    command=marcar).grid(column=0, row=7, sticky=W)
Radiobutton(
    window, 
    text="Femenino",
    value="Femenino",
    variable=option,
    command=marcar).grid(column=0, row=8, sticky=W)
marcado = Label(window)
marcado.grid(column=0, row=9)

# Option menu
def marcarOpcionMenu():
    seleccionado.config(text=opcion.get(), bg="pink", fg="green")

opcion = StringVar()
opcion.set("Opcion 1")
Label(window, text="Selecciona una opción").grid(column=1, row=6)
select = OptionMenu(window, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(column=1, row=7)
Button(window, text="Seleccionar", command=marcarOpcionMenu).grid(column=1, row=8)
seleccionado = Label(window)
seleccionado.grid(column=1, row=9)

window.mainloop()