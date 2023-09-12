"""
Hacer una calculadora que tengas 
- Dos campos de texto
- 4 botones con las operaciones
- Mostrar el resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox as MessageBox

class Calculadora:
    def __init__(self, alertas):
        self.number1 = StringVar()
        self.number2 = StringVar()
        self.result = StringVar()
        self.alertas = alertas

    def clearValues(self):
        self.number1.set("")
        self.number2.set("")

    def suma(self):
        try:
            self.result.set(float(self.number1.get()) + float(self.number2.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos.")
            self.clearValues()
        
    def resta(self):
        try:
            self.result.set(float(self.number1.get())- float(self.number2.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos.")
            self.clearValues()

    def multiplica(self):
        try:
            self.result.set(float(self.number1.get())* float(self.number2.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos.")
            self.clearValues()

    def divide(self):
        try:
            self.result.set(float(self.number1.get())/ float(self.number2.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos.")
            self.clearValues()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"{self.result.get()}")
        self.clearValues()

window = Tk()
window.geometry("300x300")
window.config(bd=25)
window.title("Calculadora")

calculadora = Calculadora(MessageBox)


marco = Frame(window, width=170, height=150)
marco.config(bd=5, relief=SOLID, padx=5, pady=5)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)
Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=calculadora.number1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=calculadora.number2, justify="center").pack()

Button(marco, text="+", command=calculadora.suma).pack(side="left", padx=10, pady=10, fill=X, expand=YES)
Button(marco, text="-", command=calculadora.resta).pack(side="left", padx=10, pady=10, fill=X, expand=YES)
Button(marco, text="x", command=calculadora.multiplica).pack(side="left", padx=10, pady=10, fill=X, expand=YES)
Button(marco, text="/", command=calculadora.divide).pack(side="left", padx=10, pady=10, fill=X, expand=YES)

window.mainloop()