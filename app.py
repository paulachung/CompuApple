from flask import Flask, redirect, request, jsonify, render_template, url_for, flash, session, make_response
from mysql.connector import Error
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import mysql.connector
import pymysql
import os
import users
import addProduct
import updatep
import deleteProduct
import mysql
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__)
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# se guardan las imágenes subidas
UPLOAD_FOLDER = 'static/uploads/'  # Carpeta de las imágenes
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  
app.secret_key = 'compu_apple'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'tecnologia_v3',
    'port': 3307
}
def connection():
  # Configuración de la conexión a la base de datos
  conn = pymysql.connect(
    host= 'localhost',
    user= 'root',  
    password= '',
    port= 3307,
    database= "tecnologia_v3",
    cursorclass=MySQLdb.cursors.DictCursor
  )
  return conn
# Conectar a la base de datos
def connect_db():
    return mysql.connector.connect(**db_config)
# Inicializar el módulo de usuarios y pasar la configuración de la DB
users.init_app(app, db_config)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/aboutUs')
def about_us():
    return render_template('aboutUs.html')

@app.route('/add-product', methods=['POST'])
def add():
    addProduct.addProduct(app)
    jsonify({"Response":"Producto agregado"})
    return redirect(url_for("admin"))

@app.route('/admin', methods=["POST","GET"])
def admin():
    if 'is_admin' in session and session['is_admin']:
       print("en admin")
       try:
            conn = connect_db()
            cursor = conn.cursor(dictionary=True)

            # Consultas para cada tabla
            cursor.execute("SELECT * FROM mac")
            mac_products = cursor.fetchall()

            cursor.execute("SELECT * FROM iphone")
            iphone_products = cursor.fetchall()

            cursor.execute("SELECT * FROM ipad")
            ipad_products = cursor.fetchall()

            cursor.execute("SELECT * FROM airpods")
            airpods_products = cursor.fetchall()
            
            cursor.execute("SELECT * FROM applewatch")
            applewatch_products = cursor.fetchall()
            
            cursor.execute("SELECT * FROM applevisionpro")
            applevisionpro_products = cursor.fetchall()
            # Combinar todos los productos en una sola lista
            products = mac_products + iphone_products + ipad_products + airpods_products + applevisionpro_products + applewatch_products
            cursor.close()
            conn.close()
            
            return render_template('admin.html', products=products)
       except Exception as e:
          flash("Error al cargar admin, verifica la conexion a la bd") 
          print("Error al cargar admin", e) 
          return jsonify({"Error":"Error al cargar admin"})
    else:
        return redirect('/index')
# {
#     "error": "1146 (42S02): Table 'compuappledb.products' doesn't exist"
# }
    
#eliminar producto
@app.route('/delete/<int:product_id>/<string:producttype>')
def delete_product(product_id, producttype):
    deleteProduct.delete(product_id, producttype)
    jsonify({"Response":"Producto eliminado"})
    return redirect(url_for("admin"))

# Ruta para actualizar un registro existente
@app.route('/update/<int:product_id>/<string:producttype>')
def update(product_id, producttype):
    try:
        # Validar el tipo de producto
        valid_product_types = ["mac", "iphone", "airpods", "applewatch", "ipad", "applevisionpro"]
        if producttype not in valid_product_types:
            flash("Tipo de producto no válido.")
            return redirect(url_for("admin"))
        print("")
        # Conectar a la base de datos
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        
        # Consultar el producto en la tabla correspondiente
        cursor.execute(f"SELECT * FROM {producttype} WHERE id=%s", (product_id,))
        product = cursor.fetchone()
        
        if product:
            return render_template("update.html", product=product)
        else:
            flash("El producto no existe en la base de datos")
            return redirect(url_for("admin"))
        
    except Exception as e:
        flash("Ocurrió un error al intentar obtener el producto: " + str(e))
        return redirect(url_for('admin'))
    
    finally:
        # Cerrar el cursor y la conexión
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@app.route("/update_product/<int:product_id>/<string:producttype>", methods=["POST"])
def update_product(product_id, producttype):
    producttype = request.form["producttype"]
    print(producttype)
    updatep.updatep(product_id, producttype)
    return redirect(url_for('admin'))

def get_products_by_type(producttype):
    # Conectar a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)  # Usar dictionary=True para obtener los resultados como diccionarios

    # Consulta para obtener los productos del tipo especificado
    query = f"SELECT * FROM {producttype}"  # El nombre de la tabla se usa directamente según el tipo de producto

    try:
        cursor.execute(query)
        products = cursor.fetchall() 
# Obtener todos los registros
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        products = []
    finally:
        # Cerrar la conexión a la base de datos
        cursor.close()
        conn.close()

    return products

# Ruta para obtener productos de un tipo específico
# @app.route('/get-products', methods=['GET'])
# def get_products():
#     product_type = request.args.get('type')  # Obtener el tipo de producto desde los parámetros de consulta
#     if not product_type:
#         return jsonify({'error': 'Tipo de producto no especificado'}), 400
    
#     # Obtener los productos de la base de datos según el tipo
#     products = get_products_by_type(product_type)

#     return jsonify({'products': products})

@app.route("/cart")
def cart():
    return render_template("carrito.html")

@app.route("/products")
def products():
    try:
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)

        # Consultas para cada tabla
        cursor.execute("SELECT * FROM mac")
        mac_products = cursor.fetchall()

        cursor.execute("SELECT * FROM iphone")
        iphone_products = cursor.fetchall()

        cursor.execute("SELECT * FROM ipad")
        ipad_products = cursor.fetchall()

        cursor.execute("SELECT * FROM airpods")
        airpods_products = cursor.fetchall()
        
        cursor.execute("SELECT * FROM applewatch")
        applewatch_products = cursor.fetchall()
        
        cursor.execute("SELECT * FROM applevisionpro")
        applevisionpro_products = cursor.fetchall()
        # Combinar todos los productos en una sola lista
        products = mac_products + iphone_products + ipad_products + airpods_products + applevisionpro_products + applewatch_products
        print(products)
        cursor.close()
        conn.close()
        return render_template('products.html', products=products)
    except Exception as e:
        flash("Error al cargar products, verifica la conexion a la bd") 
        print("Error al cargar products") 
        return jsonify({"Error":"Error al cargar products" + e})

@app.route('/mostrar_tabla')
def mostrar_tabla():
    try:        
        print("entro mostrar")
        conn = connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT `id`, `img`, `productName`, `price`, `color`, `dimensiones`, `screenSizeIphone`, `resolutionIphone`, `resistenciaIphone`, `procesadorIphone`, `camaraIphone`, `faceidIphone`, `memoryIphone`, `geolocalizacion`, `reproduccionIphone`, `sensoresIphone`, `grabacionIphone`, `siriIphone`, `bateriaIphone` FROM `iphone`")
        iphones = cursor.fetchall()    
        print(iphones)
        cursor.close()
        conn.close()
        
        datos = cursor.fetchall()  # Obtener todos los registros
        print("en try")
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
    
if __name__ == '__main__':
    app.run(debug=True) 