"""
Hacer un script que pida al usuario la calificación de 10 alumnos
mostrar en pantalla la cantidad de alumnos aprobado y reprobados
"""
number_students = int(input("Escribe el número de estudiantes para calificar: "))
approved = 0
failed = 0
for i in range(1,number_students + 1):
    score = int(input(f"Introduce la calificación del alumno {i}: "))
    if score < 6:
        failed += 1
    else:
        approved += 1
print(f"Cantidad de alumnos aprobados: {approved}")
print(f"Cantidad de alumnos reprobados: {failed}")
