"""
Crear un programa que tenga lo siguiente:
- Una ventana
- Tamaño fijo de la ventana
- Ventana no redimensionable
- Un menú (Inicio, Añadir, Información, Salir)
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla principal (home)
- Obsion de salir
"""
from tkinter import *
from tkinter import ttk

# Definis ventana
window = Tk()
window.title("Proyecto con tkinter")
#window.geometry("600x400")
window.minsize(500, 500)
window.resizable(0, 0)

# Pantallas
def pageHome():
    # Montando pantalla Inicio
    # Encabezado
    home_label.config(fg="white", bg="black", font=("Arial", 30), padx=255, pady=20, )
    home_label.grid(column=0, row=0)
    products_box.grid(column=0, row=1)
    products_table.grid(column=0, row=1, columnspan=2)
    products_table.heading("#0", text="Producto", anchor=W)
    products_table.heading("#1", text="Precio", anchor=W)
    products_table.heading("#2", text="Descripción", anchor=W)
    
    """
    #Listar productos
    for product in products:
        if len(product) == 3:
            product.append("Agregado")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="--------------------------------").grid()
            print(product)
    """
    for product in products:
        if len(product) == 3:
            product.append("Agregado")
            products_table.insert("", 0, text=product[0], values=(product[1],product[2]))            

    # Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()
    return True

def pageAdd():
    # Montando pantalla agregar
    # Encabezado
    add_label.config(fg="white", bg="black", font=("Arial", 30), padx=150, pady=20)
    add_label.grid(column=0, row=0, columnspan=15)

    # Formulario
    add_frame.grid(column=0, row=1)
    add_product_label.grid(column=0, row=1, padx=5, pady=10, sticky=E)
    add_product_entry.grid(column=1, row=1, padx=5, pady=5, sticky=W)
    add_price_label.grid(column=0, row=2, padx=5, pady=5, sticky=E)
    add_price_entry.grid(column=1, row=2, padx=5, pady=5, sticky=W)
    add_description_label.grid(column=0, row=3, padx=5, pady=5, sticky=NE)
    add_description_entry.grid(column=1, row=3, padx=5, pady=5, sticky=W)
    boton = Button(add_frame, text="Guardar")
    boton.grid(row=6, column=1, sticky=W)
    boton.config(bg="black", fg="white", padx=5, pady=5, command=saveProducts)
    boton_home = Button(add_frame, text="Ver productos")
    boton_home.grid(row=6, column=1, sticky=E)
    boton_home.config(bg="green", fg="white", padx=5, pady=5, command=pageHome)
    # Ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()
    products_table.grid_remove()

    return True

def pageInfo():
    # Montando pantalla información
    # Encabezado
    info_label.config(fg="white", bg="black", font=("Arial", 30), padx=196, pady=20)
    info_label.grid(column=0, row=0)
    data_label.grid(column=0, row=1)
    # Ocultar otras pantallas
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()
    products_table.grid_remove()
    return True

def saveProducts():
    products.append([
        product_name.get(),
        price_product.get(),
        add_description_entry.get("1.0", "end-1c")#Para gurdar los datos de la caja de texto en el arreglo
    ])
    print(products)
    clearValues()
    clearTextInput()

def clearValues():
    product_name.set("")
    price_product.set("")

def clearTextInput():
    add_description_entry.delete(1.0, END)
# Definiendo variables
products = []
product_name = StringVar()
price_product = StringVar()
description_product = StringVar()
# Frame para guardar el formulario
add_frame = Frame(window)

# Definir campos de pantalla
home_label = Label(window, text="Inicio")
products_box = Frame(window, width=250)
Label(products_box).grid(row=0)
products_table = ttk.Treeview(height=12, columns=("#0, #1"))


add_label = Label(window, text="Agregar producto")
info_label = Label(window, text="Información")
data_label = Label(window, text="Alexis Arturo Solís - 2023")

# Definir campos de formulario
add_product_label = Label(add_frame, text="Nombre:")
add_product_entry = Entry(add_frame, textvariable=product_name)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_product)

add_description_label = Label(add_frame, text="Descripción:")
add_description_entry = Text(add_frame)
add_description_entry.config(width=35, height=7, font=("Consolas", 11), padx=15, pady=15)



# Cargar pantalla inicio
pageHome()

# Menú superior
home_menu = Menu(window)
home_menu.add_command(label="Inicio", command=pageHome)
home_menu.add_command(label="Añadir", command=pageAdd)
home_menu.add_command(label="Información", command=pageInfo)
home_menu.add_command(label="Salir", command=window.quit)

# Cargar menu
window.config(menu=home_menu)

# Cargar ventana
window.mainloop()
