import usuarios.conexion as conexion 

connect = conexion.connect_database()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self, user_id, title = "", description = ""):
        self.user_id = user_id
        self.title = title
        self.description = description

    def saveNote(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        note = (self.user_id, self.title, self.description)
        cursor.execute(sql,note)
        database.commit()
        result = [cursor.rowcount, self]
        return result
    
    def showNotes(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.user_id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def deleteNote(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.user_id} AND titulo LIKE '%{self.title}%'"
        cursor.execute(sql)
        database.commit()
        result = [cursor.rowcount, self]
        return result
    
    def updateNote(self):
        print(f"Descripcion: {self.description}")
        print(f"Id usuario: {self.user_id}")
        print(f"Título: {self.title}")
        sql =  f"UPDATE notas SET descripcion = '{self.description}' WHERE usuario_id = '{self.user_id}' and titulo ='{self.title}'"
        cursor.execute(sql)
        database.commit()
        result = [cursor.rowcount, self]
        return result