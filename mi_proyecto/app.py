from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

#conexion a mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.mi_base_de_datos
coleccion = db.mi_coleccion

@app.route("/")
def index():
  datos = list(coleccion.find())
  return render_template("index.html", datos=datos)