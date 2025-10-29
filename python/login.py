import pymysql
from conexion import Conect

def login(usuario, clave):
    dbmethod = Conect()
    db = dbmethod.conexiondb()

    if db is None:
        print("La conexion ha fallado")
        return
    cursor = db.cursor()
    sql = "Select username, password from usuarios where username = %s and password = %s"
    cursor.execute(sql, (usuario, clave))
    result = cursor.fetchone()

    if result: 
        print("Conexion exitosa")
    else:
        print("Uno o mas datos son incorrectos")