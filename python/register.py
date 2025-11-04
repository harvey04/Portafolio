from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from conexion import Conect
from flask  import AppConfig

config = AppConfig()

class registro(AppConfig):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/register", methods=["POST", "GET"])
    def registro(username, password):
   
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            datamethod = Conect()
            data = datamethod.conexiondb()
            if data is None:
                print("Conexion fallida")

            try:

                cursordb = data.cursor()
                sql = "Insert into usuarios(username, password) values (%s, %s)"
                cursordb.execute(sql, (username, password))
                data.commit()

                flash("Usuario registrado correctamente")
                return redirect(url_for("index"))
    
            except pymysql.MySQLError as e:
                flash(f"Error al registrar {e}")
                return redirect(url_for("index"))
        
        return render_template("register.html")