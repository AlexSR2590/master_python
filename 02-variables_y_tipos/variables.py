"""Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear muchas variables
y que cada una tenga un dato distinto.
"""
print("----------Variables----------")
text = "Esto es un texto."
number = 25
decimal = 15.9
print(text)
print(number)
print(decimal)

print("----------Concatenación----------")
name = "Alexis"
lastName = "Solís"
age = 33
print(name + " " + lastName + " " + str(age))
print(f"{name} {lastName} {age}")
print("{} {} {}".format(name, lastName, age))