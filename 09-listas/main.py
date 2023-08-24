# Listas (arrays)
films = ["Batman", "Spiderman", "Superman"]
years = list(range(1990, 2024))
#print(films)
planets = list(("Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturo", "Urano", "Neptuno", "Pluton"))
print(planets)
#print(years)
varied = ["Alexis", 33, False, 1.70]
#print(varied)

# indices
print(planets[2])
print(planets[-2])
print(planets[2:7])

# Añadir elementos a una lista
planets.append("Proxima Centauri")
print(planets)

# Recorrer lista
print("\n########## Listado de planetas ##########")
for planet in planets:
    print(f"{planets.index(planet)}.- {planet}")

add_planet = "parar"

while add_planet != "parar":
    planets.append(add_planet)
    add_planet = input("Escribe el nombre del planeta o escribe 'parar' para detener el programa: ")
else:
    print(planets)

# Listas multidimensionales
print("\n************* Listado de contactos *************")
contacts = [
    [
        'Alexis',
        'alex@correo.com'
    ],
    [
        'Andi',
        'andi@correo.com',
    ],
    [
        'Carlos',
        'carlos@correo.com'
    ],
    [
        'Alondra',
        'alondra@correo.com'
    ]
]
print(contacts)
print(f"Nombre: {contacts[3][0]}")
print(f"Email: {contacts[3][1]}")
print("\n************* CONTACTOS *************")
for contact in contacts:
    for element in contact:
        if contact.index(element) == 0:
            print(f"Nombre: {element}")
        else: 
            print(f"Email: {element}")
    print("\n")