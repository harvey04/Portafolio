from flask import Flask

class AppConfig:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = "clave secreta"