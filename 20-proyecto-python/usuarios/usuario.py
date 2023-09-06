from datetime import datetime
import hashlib
import usuarios.conexion as conectiondb

connect = conectiondb.connect_database()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, name, last_name, email, passwd):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.passwd = passwd

    def register(self):
        date = datetime.now()
        # Cifrar la contraseña
        encrypt_passwd = hashlib.sha256()
        encrypt_passwd.update(self.passwd.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.last_name, self.email, encrypt_passwd.hexdigest(), date)
        try:
            cursor.execute(sql,user)
            database.commit()
            result = [cursor.rowcount, self]
        except Exception as e:
            print(e)
            result = [0, self]
        return result

    def identify(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND passwd = %s "
        encrypt_passwd = hashlib.sha256()
        encrypt_passwd.update(self.passwd.encode('utf8'))
        user = (self.email, encrypt_passwd.hexdigest())
        cursor.execute(sql, user)
        result = cursor.fetchone()
        return result
    