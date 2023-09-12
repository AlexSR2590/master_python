from tkinter import *
window = Tk()
#window.geometry("500x500")

texto = Label(window, text="Bienvenido a mi programa" )
texto.config(
    fg="white", 
    bg="black", 
    padx=50, 
    pady=20,
    font=("Arial", 30)
    )
texto.pack(side=TOP)

texto = Label(window, text= "Alexis Arturo")
texto.config(
    height=3,
    bg="orange",
    fg="white",
    font=("Arial", 18), 
    padx=10,
    pady=20,
    cursor="spider"
    )
texto.pack(side= TOP, fill=X, expand=YES)

texto = Label(window, text="Basico 1")
texto.config(
    height=3,
    bg="red",
    fg="white",
    font=("Arial", 18), 
    padx=10,
    pady=20,
    cursor="circle"
    )
texto.pack(side= LEFT, fill=X, expand=YES)

texto = Label(window, text="Basico 2")
texto.config(
    height=3,
    bg="green",
    fg="black",
    font=("Arial", 18), 
    padx=10,
    pady=20,
    cursor="circle"
    )
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(window, text="Basico 3")
texto.config(
    height=3,
    bg="purple",
    fg="white",
    font=("Arial", 18), 
    padx=10,
    pady=20,
    cursor="circle"
    )
texto.pack(side=LEFT, fill= X, expand=YES)

window.mainloop()