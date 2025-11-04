import pymysql

class Conect():

    def conexiondb(self):
        try:    
            db = pymysql.connect(host="localhost", user="root", password="", database="prueba")
            cursor= db.cursor()
            cursor.execute("SELECT VERSION()")

            version = cursor.fetchone()
            print(f"Conexion exitosa version mysql {version[0]}")
            return db
        except pymysql.MySQLError as e:
            print(f"Error de conexion {e}")
            return None
        
    
if __name__ == "__main__":
    con = Conect()
    con.conexiondb()