"""
Hacer una calculadora que tengas 
- Dos campos de texto
- 4 botones con las operaciones
- Mostrar el resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox as MessageBox

window = Tk()
window.geometry("300x300")
window.config(bd=25)
window.title("Calculadora")

def clearValues():
    number1.set("")
    number2.set("")

def suma():
    try:
        result.set(float(number1.get()) + float(number2.get()))
        mostrarResultado()
    except:
        MessageBox.showerror("Error", "Introduce bien los datos.")
        clearValues()
    
def resta():
    try:
        result.set(float(number1.get())- float(number2.get()))
        mostrarResultado()
    except:
        MessageBox.showerror("Error", "Introduce bien los datos.")
        clearValues()

def multiplica():
    try:
        result.set(float(number1.get())* float(number2.get()))
        mostrarResultado()
    except:
        MessageBox.showerror("Error", "Introduce bien los datos.")
        clearValues()

def divide():
    try:
        result.set(float(number1.get())/ float(number2.get()))
        mostrarResultado()
    except:
        MessageBox.showerror("Error", "Introduce bien los datos.")
        clearValues()

def mostrarResultado():
    MessageBox.showinfo("Resultado", f"{result.get()}")
    clearValues()

number1 = StringVar()
number2 = StringVar()
result = StringVar()

marco = Frame(window, width=170, height=150)
marco.config(bd=5, relief=SOLID, padx=5, pady=5)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)
Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=number1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=number2, justify="center").pack()

Button(marco, text="+", command=suma).pack(side="left", padx=10, pady=10, fill=X, expand=YES)
Button(marco, text="-", command=resta).pack(side="left", padx=10, pady=10, fill=X, expand=YES)
Button(marco, text="x", command=multiplica).pack(side="left", padx=10, pady=10, fill=X, expand=YES)
Button(marco, text="/", command=divide).pack(side="left", padx=10, pady=10, fill=X, expand=YES)

window.mainloop()