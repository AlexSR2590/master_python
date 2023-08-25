"""
Crear una lista con los siguientes datos.
acción      aventura           deportes
gta           mario              fifa21
cod           crash              motogp21
pugb          zelda              pro21
"""
videogames = {
    'Accion': ['gta', 'cod', 'pugb'],
    'Aventura': ['mario', 'crash', 'zelda'],
    'Deportes': ['fifa21', 'motogp21', 'pro21']
}
for category in videogames:
    print(f"Categoría: {category} ------> {videogames[category]}")

print("\n---------------------------------------")

table = [
    {
        'categoria': 'accion',
        'juegos': ['gta', 'cod', 'pugb']
    },
    {
        'categoria': 'aventura',
        'juegos': ['mario', 'crash', 'zelda']
    },
    {
        'categoria': 'deportes',
        'juegos': ['fifa21', 'motogp21', 'pro21']
    }
]

for categoria in table:
    print(f"--------------{categoria['categoria']}------------------")
    for juego in categoria['juegos']:
        print(f"{juego}")
   