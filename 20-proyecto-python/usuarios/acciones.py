from usuarios import usuario as modelo
import notas.acciones

class Acciones:
    def register(self):
        print("\nIngresa los datos para registrarte.")
        name = input("Escribe tu nombre: ")
        last_name = input("Escribe tus apellidos: ")
        email = input("Escribe tu correo electrónico: ")
        passwd = input("Escribe tu contraseña: ")
        user = modelo.Usuario(name, last_name, email, passwd)
        register = user.register()
        if register[0] >= 1:
            print(f"\nBienvenido {register[1].name}, te has registrado con el correo {register[1].email}")
        else:
            print("\nNo te has registrado correctamente.")
    def login(self):
        print("\nIngresa tus datos para iniciar seción.")
        try:
            email = input("Escribe tu correo electrónico: ")
            passwd = input("Ingresa tu contraseña: ")
            user = modelo.Usuario('', '', email, passwd)
            login = user.identify()
            if email == login[3]:
                print(f"Bienvenido {login[1]}, Fecha de registro en sistema: {login[5]}")
                self.menuActions(login)
        except Exception as e:
            #print(e)
            print(type(e).__name__)
            print("Fallo al inicio de seción, verifica tus datos.")
    
    def menuActions(self, user):
        print("""
        - Crear nota (crear)
        - Mostrar nota (mostrar)
        - Editar nota (editar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        \n""")
        action_menu = input("¿Qué acción quieres hacer?: ").lower()
        note_actions = notas.acciones.Acciones()
        if action_menu == "crear":
            note_actions.createNote(user)
            print("Nota guardada....\n")
            self.menuActions(user)
        elif action_menu == "mostrar":
            print("Vamos a mostrar tus notas...")
            note_actions.showNotes(user)
            self.menuActions(user)
        elif action_menu == "editar":
            print("\nLista de notas que puedes editar.\n")
            note_actions.showNotes(user)
            note_actions.updateNotes(user)
            self.menuActions(user)
        elif action_menu == "eliminar":
            print("\nLista de notas que puedes eliminar.\n")
            note_actions.showNotes(user)
            note_actions.deleteNotes(user)
            self.menuActions(user)
        elif action_menu == "salir":
            print(f"Hasta pronto {user[1]}, un placer ayudarte en tus notas.")
            exit()
        else:
            print("Lo siento, no entiendo la acción, ingresa los datos correctamente....")
            
    