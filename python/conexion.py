import pymysql

class Conect():

    def conexiondb(self):
        try:    
            db = pymysql.connect(host="localhost", user="root", password="password", database="prueba")
            print("Conexion exitosa")
            return db
        except:
            print("Error de conexion")
            return None