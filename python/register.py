from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from conexion import Conect

app.Flask("name")
app.secret_key= "Clave secreta"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registro", method=[POST, GET])
def registro(username, password):
    datamethod = Conect()
    data = datamethod.conexiondb()

    if data is None:
        print("Conexion fallida")

    try:

        cursordb = data.cursor()
        sql = "Insert into usuarios(username, password) values (%s, %s)"
        cursordb.execute(sql(username, password))
        data.commit()

        print("Registro exitoso")
    
    except pymysql.MySQLError as e:
        print(f"Error al registrar {e}")