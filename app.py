from flask import Flask, request, redirect, render_template, jsonify, url_for
# import mysql.connector
import os
import pymysql

app = Flask(__name__)

def connection():
  # Configuración de la conexión a la base de datos
  conn = pymysql.connect(
      host= 'localhost',
      user= 'root',  
      password= '',
      port= 3307,
      database= "tecnologia"
  )
  
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/add", methods=['POST'])
def add():    
    print("entro ================")
    if request.method == 'POST':
        print("2==================")
        # Obtener datos del formulario
        nombre = request.form['product-name']
        descripcion = request.form['product-description']
        precio = request.form['product-price']
        categoria = request.form['product-category']
        imagen = request.files['product-image']
        print(categoria, '-----')

        # Guardar la imagen en una carpeta de tu proyecto
        if imagen and imagen.filename != '':
            imagen_path = os.path.join('static/img/', imagen.filename)
            imagen.save(imagen_path)
        else:
            imagen_path = None

        # Conectar a la base de datos y guardar el producto
        try:
            conn = connection()
            cursor = conn.cursor()
            # Determinar la tabla en función de la categoría
            query = f"INSERT INTO {categoria} (nombre, descripcion, precio, imagen_path) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre, descripcion, precio, imagen_path))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/admin')
        except pymysql.connector.Error as err:
            print(f"Error: {err}")
            return "Hubo un error al guardar el producto en la base de datos."




@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        while True:
            nombre = request.form['nombre'] 
            password = request.form['password']
            # Conectar a la base de datos y verificar el usuario
            try:
                conn = connection()
                cursor = conn.cursor()
                # Verificar si el usuario y contraseña existen
                query = "SELECT * FROM users WHERE nombre = %s AND password = %s"
                cursor.execute(query, (nombre, password))
                user = cursor.fetchone()

                cursor.close()
                conn.close()

                if user:
                    # Si el usuario es válido, redirigir a la página de productos
                    # return jsonify({"redirect": "/products"}), 200
                    return render_template("/products.html")
                else:
                    # Si el login falla, enviar un error
                    return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

            except pymysql.MySQLError as err:
                print(f"Error: {err}")
                return jsonify({"error": "Error de servidor"}), 500
    return render_template("login.html")

# Ruta para mostrar la página de productos después de iniciar sesión
@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutUs.html')

if __name__ == '__main__':
    app.run(debug=True)
