frase ="Esto es una variable Global"

def variableLocal():
    frase = "Esto es una variable Local"
    return frase

print(f"Contenido variable global: {frase}")
print(f"Contenido variable local: {variableLocal()}")
