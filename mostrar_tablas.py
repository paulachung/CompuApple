from flask import Flask, redirect, request, jsonify, render_template, url_for, flash, session
from mysql.connector import Error
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import mysql.connector
import pymysql
import mysql
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__)
def connection():
  # Configuración de la conexión a la base de datos
  conn = pymysql.connect(
    host= 'localhost',
    user= 'root',  
    password= '',
    port= 3307,
    database= "tecnologia_v3"
  )
  return conn

@app.route('/mostrar_tabla')
def mostrar_tabla():
    try:
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM iphone")  # Consulta para obtener todos los registros
        datos = cursor.fetchall()  # Obtener todos los registros
       
        # Obtener nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]

        cursor.close()
        conn.close()
        return render_template('mostrar_tabla.html', datos=datos, column_names=column_names)
    except Error as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return "Error en la conexión a la base de datos"
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return "Ocurrió un error al recuperar los datos"
      
      
# @app.route('/mostrar_tabla')
# def mostrar_tabla():
#     conn = connection()
#     cursor = conn.cursor()    
#     cursor.execute("SELECT * FROM mac")  # Reemplaza `tu_tabla` con el nombre de tu tabla
#     datos = cursor.fetchall()  # Obtener todos los registros
#     cursor.close()
#     conn.close()
#     return render_template('mostrar_tabla.html', datos=datos)
  
# app.run(port="5500", debug=True)