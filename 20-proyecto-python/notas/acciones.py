from notas import nota as modelo

class Acciones:
    def createNote(self, user):
        print(f"\n{user[1]} Vamos a crear una nueva nota...")
        title = input("Escribe el título de tu nota: ")
        description = input("Escribe el contenido de tu nota: ")
        note = modelo.Nota(user[0], title, description)
        save_note = note.saveNote()
        if save_note[0] >= 1:
            print(f"Se ha guardado la nota: {title} ")
        else: 
            print(f"Algo salió mal, no se ha a guardado la nota: {title}")
    
    def showNotes(self, user):
        print(f"\n{user[1]}, estas son las notas que tienes guardadas...\n")
        note = modelo.Nota(user[0])
        notes = note.showNotes()
        for i in notes:
            print(f"Título: {i[2]}\nContenido: {i[3]}\n")
            print("--------------------------------------------------------------------\n")

    def deleteNotes(self, user):
        print(f"\n{user[1]}, Vamos a eliminar una nota...\n")
        title_note = input("Escribe el título de la nota que deseas eliminar: ")
        note = modelo.Nota(user[0], title_note)
        delete_note = note.deleteNote()
        if delete_note[0] >= 1:
            print(f"Se ha eliminado la nota: {note.title}")
        else:
            print(f"No se ha borrado la nota: {note.title}")

    def updateNotes(self, user):
        print(f"\n{user[1]}, vamos a editar una nota...\n")
        title_note = input("Escribe el títuto de la nota a editar: ")
        new_description = input("Escribe el nuevo contenido de la nota: ")
        note = modelo.Nota(user[0], title_note, new_description)
        update_note = note.updateNote()
        if update_note[0] >= 1:
            print(f"Se ha editado la nota: {note.title}")
        else:
            print(f"No se editó la nota: {note.title}")