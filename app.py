from flask import Flask, redirect, request, jsonify, render_template, url_for, flash
from mysql.connector import Error
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import mysql.connector
import pymysql
import os
import users
import addProduct
import deleteProduct

app = Flask(__name__)

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
    database= "tecnologia_v3"
  )
  return conn
# Conectar a la base de datos
def connect_db():
    return mysql.connector.connect(**db_config)
# Inicializar el módulo de usuarios y pasar la configuración de la DB
users.init_app(app, db_config)

@app.route("/selectIphones", methods=["GET"])
def selectIphones():
    try:
        conn = connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT `id`, `img`, `productName`, `price`, `color`, `dimensiones`, `screenSizeIphone`, `resolutionIphone`, `resistenciaIphone`, `procesadorIphone`, `camaraIphone`, `faceidIphone`, `memoryIphone`, `geolocalizacion`, `reproduccionIphone`, `sensoresIphone`, `grabacionIphone`, `siriIphone`, `bateriaIphone` FROM `iphone`")
        iphones = cursor.fetchall()    
        
        cursor.close()
        conn.close()
        return render_template('products.html', data=iphones)
        # return jsonify({"Response": iphones})
        
    except Exception as e:
        print("error en la coneccion",e)
        return jsonify({"error": "Error en la conexión o en la operación"}), 500


@app.route('/')
def home():
    return redirect('/index')

@app.route('/index')
def index():
    # return redirect('/admin')
    return render_template('index.html')

# Agregar un nuevo producto
@app.route('/products', methods=["GET"])
def products():
    return selectIphones()

@app.route('/aboutUs')
def about_us():
    return render_template('aboutUs.html')

@app.route('/add-product', methods=['POST'])
def add_product():
    flash(addProduct.addProduct(app))
    return redirect(url_for("admin_page"))


#mostrar 
@app.route('/admin')
def admin_page():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    # Consultas para cada tabla
    cursor.execute("SELECT *, 'mac' AS product_type FROM mac")
    mac_products = cursor.fetchall()

    cursor.execute("SELECT *, 'iphone' AS product_type FROM iphone")
    iphone_products = cursor.fetchall()

    cursor.execute("SELECT *, 'ipad' AS product_type FROM ipad")
    ipad_products = cursor.fetchall()

    cursor.execute("SELECT *, 'airpods' AS product_type FROM airpods")
    airpods_products = cursor.fetchall()
    
    cursor.execute("SELECT *, 'applewatch' AS product_type FROM applewatch")
    applewatch_products = cursor.fetchall()
    
    cursor.execute("SELECT *, 'applevisionpro' AS product_type FROM applevisionpro")
    applevisionpro_products = cursor.fetchall()
    # Combinar todos los productos en una sola lista
    # products = mac_products + iphone_products + ipad_products + airpods_products
    cursor.close()
    conn.close()
    return render_template('admin.html', mac=mac_products, iphone=iphone_products, ipad=ipad_products, airpods=airpods_products, applewatch=applewatch_products, applevisionpro=applevisionpro_products)

{
    "error": "1146 (42S02): Table 'compuappledb.products' doesn't exist"
}
# @app.route('/login', methods=["GET","POST"])
# def login():
#     try:
#         if request.method == "POST":
            
#             return redirect(url_for("admin"))
#     except Exception as e:
#         print("Error en /login")
#         return render_template("login.html")
#     return render_template("login.html")
    
#eliminar producto
@app.route('/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    deleteProduct.delete(app,product_id)
    return jsonify({"Response":"Producto eliminado"})
        

#editar producto

@app.route('/edit-product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'GET':
        cursor.execute("SELECT * FROM mac WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('edit-product.html', product=product)

    elif request.method == 'POST':
        # Recibir datos del formulario y actualizar el producto
        product_name = request.form['productName']
        price = request.form['price']
        color = request.form['color']
        # Actualizar en la base de datos
        cursor.execute("""
            UPDATE mac 
            SET productName = %s, price = %s, color = %s
            WHERE id = %s
        """, (product_name, price, color, product_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/admin')

def get_products_by_type(product_type):
    # Conectar a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)  # Usar dictionary=True para obtener los resultados como diccionarios

    # Consulta para obtener los productos del tipo especificado
    query = f"SELECT * FROM {product_type}"  # El nombre de la tabla se usa directamente según el tipo de producto

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
@app.route('/get-products', methods=['GET'])
def get_products():
    product_type = request.args.get('type')  # Obtener el tipo de producto desde los parámetros de consulta
    if not product_type:
        return jsonify({'error': 'Tipo de producto no especificado'}), 400
    
    # Obtener los productos de la base de datos según el tipo
    products = get_products_by_type(product_type)

    return jsonify({'products': products})

if __name__ == '__main__':
    app.run(debug=True) 