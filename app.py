from flask import Flask, redirect, request, jsonify, render_template, url_for, flash, session
from mysql.connector import Error
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import mysql.connector
import pymysql
import os
import users
import addProduct
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
    return redirect(url_for("/admin"))

@app.route('/admin', methods=["POST","GET"])
def admin():
    if 'is_admin' in session and session['is_admin']:
       print("admin")
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
            return render_template('admin.html', products=products)
       except Exception as e:
          flash("Error al cargar admin, verifica la conexion a la bd") 
          print("Error al cargar admin") 
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
@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    cursor = connection.cursor()
    
    name = request.form['name']
    # Actualizar el registro en la base de datos
    cursor.execute('UPDATE tabla SET nombre = %s WHERE id = %s', (name, id))
    connection.commit()
    return redirect(url_for('index'))

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