from tkinter import *

window = Tk()
window.title("Frames | Master en python")
window.geometry("500x500")

marco_padre_top = Frame(window, width=150, height=150)
#marco_padre_top.config(bg="lightblue")
marco_padre_top.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco = Frame(marco_padre_top, width=150, height=150)
marco.config(
    bg="purple",
    bd=5,
    relief=RAISED
)
marco.pack(side=LEFT, anchor=NW)
marco.pack_propagate(False)
primer_texto = Label(marco, text="Primer marco")
primer_texto.config(
    bg="blue",
    fg="white",
    font=("Arial", 15),
    anchor=CENTER
)
primer_texto.pack(fill=Y, expand=YES)

marco = Frame(marco_padre_top, width=150, height=150)
marco.config(
    bg="green",
    bd=5,
    relief=RAISED
)
marco.pack(side=RIGHT, anchor=NE)
marco.pack_propagate(False)
segundo_texto = Label(marco, text="Segundo marco")
segundo_texto.config(
    bg="yellow",
    fg="red",
    font=("Arial", 15),
    anchor=CENTER
)
segundo_texto.pack(fill=Y, expand=YES)

marco_padre_down = Frame(window, width=150, height=150)
#marco_padre_down.config(bg="lightblue")
marco_padre_down.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre_down, width=150, height=150)
marco.config(
    bg="red",
    bd=5,
    relief=RAISED
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)
tercer_texto = Label(marco, text="Tercer marco")
tercer_texto.config(
    bg="black",
    fg="orange",
    font=("Arial", 15),
    anchor=CENTER
)
tercer_texto.pack(fill=Y, expand=YES)

marco = Frame(marco_padre_down, width=150, height=150)
marco.config(
    bg="pink",
    bd=5,
    relief=RAISED
)
marco.pack(side=RIGHT, anchor=SE)
marco.pack_propagate(False)
cuarto_texto = Label(marco, text="Cuarto marco")
cuarto_texto.config(
    bg="green",
    fg="purple",
    font=("Arial", 15),
    anchor=CENTER
)
cuarto_texto.pack(fill=Y, expand=YES)
window.mainloop()