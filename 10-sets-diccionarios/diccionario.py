"""
Diccionario es un tipo de dato que almacena un conjunto de datos (Clave - Valor) parecido a un objeto JSON
"""
person = {
    "nombre" : "ALexis",
    "apellido" : "Solís",
    "correo" : "alex@gmail.com"
}
print(type(person))
print(person)
print(person["nombre"])
print(person["apellido"])
print(person["correo"])

# Lista con diccionarios
contacts = [ 
    {
        'nombre' : 'Alondra',
        'telefono': 124654,
        'correo': 'alondra@gmail.com'
    },
    {
        'nombre' : 'Areli',
        'telefono': 5481155,
        'correo': 'areli@gmail.com'
    },
    {
        'nombre': 'Andrea',
        'telefono': 1547782,
        'correo': 'andrea@gmail.com'
    },
    {
        'nombre': 'Alexis',
        'telefono': 7569845,
        'correo': 'alexis@gmail.com'
    }
]
print(f"Nombre: {contacts[0]['nombre']}")
print(f"Telefono: {contacts[0]['telefono']}")
print(f"Correo: {contacts[0]['correo']}")
contacts[0]['nombre'] = "Alondrita"
print(f"Nombre: {contacts[0]['nombre']}")
print("\n######## Listado de contactos #########")

for contact in contacts:    
    print("\n------------------------------")
    print(f"Nombre: {contact['nombre']}")    
    print(f"Telefono: {contact['telefono']}")
    print(f"Correo: {contact['correo']}")
print("\n------------------------------")