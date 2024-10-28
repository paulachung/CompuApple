from flask import Flask, redirect, request, jsonify, render_template, url_for, flash
from mysql.connector import Error
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import mysql.connector
import pymysql
import os
import users

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
    conn = connect_db()
    cursor = conn.cursor()
    
    if 'img' not in request.files:
        return jsonify({"error": "No file part"}), 400
    img_file = request.files['img']
    if img_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Guardar la imagen en la carpeta de uploads
    filename = secure_filename(img_file.filename)
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img_file.save(img_path)

    # Recibir datos del formulario
    product_type = request.form['productType']  # Tipo de producto
    product_name = request.form['productName']  # Nombre del producto
    price = request.form['price']  # Precio del producto
    color = request.form['color']  # Color del producto

    #img_path en lugar de img
    img = img_path
    product_id = None
    
    try:
        # Insertar datos según el tipo de producto seleccionado
       if product_type == 'mac':
          dimensiones = request.form.get('dimensiones')
          screenSizeMac = request.form.get('screenSizeMac')
          capacidadMac = request.form.get('capacidadMac')
          memoriaMac = request.form.get('memoriaMac')
          procesadorMac = request.form.get('procesadorMac')
          softwareMac = request.form.get('softwareMac')
          conexionInalambricaMac = request.form.get('conexionInalambricaMac')
          audioMac = request.form.get('audioMac')
          tecladoMac = request.form.get('tecladoMac')
          camaraMac = request.form.get('camaraMac')
          formatoMac = request.form.get('formatoMac')
          bateriaMac = request.form.get('bateriaMac')

          # Insertar en la tabla 'mac'
          query = """INSERT INTO mac (productName, price, color, img, dimensiones,
                               screenSizeMac, capacidadMac, memoriaMac, procesadorMac, softwareMac, 
                               conexionInalambricaMac, audioMac, tecladoMac, camaraMac, formatoMac, bateriaMac) 
                   VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
          cursor.execute(query, (product_name, price, color, img, dimensiones,
                               screenSizeMac, capacidadMac, memoriaMac, procesadorMac, softwareMac, 
                               conexionInalambricaMac, audioMac, tecladoMac, camaraMac, formatoMac, bateriaMac))
          conn.commit()
       elif product_type == 'iphone':
            dimensiones = request.form.get('dimensiones')
            screenSizeIphone = request.form.get('screenSizeIphone')
            resolutionIphone = request.form.get('resolutionIphone')
            resistenciaIphone = request.form.get('resistenciaIphone')
            procesadorIphone = request.form.get('procesadorIphone')
            camaraIphone = request.form.get('camaraIphone')
            faceidIphone = request.form.get('faceidIphone')
            memoryIphone = request.form.get('memoryIphone')
            geolocalizacion = request.form.get('geolocalizacion')
            reproduccionIphone = request.form.get('reproduccionIphone')
            sensoresIphone = request.form.get('sensoresIphone')
            grabacionIphone = request.form.get('grabacionIphone')
            siriIphone = request.form.get('siriIphone')
            bateriaIphone = request.form.get('bateriaIphone')

           # Insertar en la tabla 'iphone'
            query = """INSERT INTO iphone (productName, price, color, dimensiones, img,
                               screenSizeIphone, resolutionIphone, resistenciaIphone, procesadorIphone, 
                               camaraIphone, faceidIphone, memoryIphone, geolocalizacion, reproduccionIphone, 
                               sensoresIphone, grabacionIphone, siriIphone, bateriaIphone) 
                      VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (product_name, price, color, dimensiones, img,
                               screenSizeIphone, resolutionIphone, resistenciaIphone, procesadorIphone, 
                               camaraIphone, faceidIphone, memoryIphone, geolocalizacion, reproduccionIphone, 
                               sensoresIphone, grabacionIphone, siriIphone, bateriaIphone))
            conn.commit()
       elif product_type == 'ipad':
             screenSizeIpad = request.form.get('screenSizeIpad')
             capacidadIpad= request.form.get('capacidadIpad')
             memoriaipad = request.form.get('memoriaipad')
             procesadorIpad = request.form.get('procesadorIpad')
             camaraIpad = request.form.get('camaraIpad')
             softwareIpad= request.form.get('softwareIpad')
             conexioninalambricaIpad = request.form.get('conexioninalambricaIpad')
             audioIpad = request.form.get('audioIpad')
             geolocalizacionIpad = request.form.get('geolocalizacionIpad')
             bateriaIpad= request.form.get('bateriaIpad')
             sensoresIpad = request.form.get('sensoresIpad')
             tuchidIpad = request.form.get('tuchIdIpad')
             siriIpad = request.form.get('siriIpad')

           # Insertar en la tabla 'ipad'
             query = """INSERT INTO ipad (productName, price, color, img,
                               screenSizeIpad, capacidadIpad, memoriaipad, procesadorIpad, camaraIpad, 
                               softwareIpad, conexioninalambricaIpad, audioIpad, geolocalizacionIpad, 
                               bateriaIpad, sensoresIpad, tuchidIpad, siriIpad) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
             cursor.execute(query, (product_name, price, color, img,
                               screenSizeIpad, capacidadIpad, memoriaipad, procesadorIpad, camaraIpad, 
                               softwareIpad, conexioninalambricaIpad, audioIpad, geolocalizacionIpad, 
                               bateriaIpad, sensoresIpad, tuchidIpad, siriIpad))
             conn.commit()
       elif product_type == 'airpods':
            batteryLifeAirpods = request.form.get('batteryLifeAirpods')
            noiseCancellation = request.form.get('noiseCancellation')
            sensoresAirpods = request.form.get('sensoresAirpods')
         
         # Insertar en la tabla 'airpods'
            query = """INSERT INTO airpods (productName, price, color, img, batteryLifeAirpods, noiseCancellation,
                               sensoresAirpods) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (product_name, price, color, img, batteryLifeAirpods, noiseCancellation,
                               sensoresAirpods))
            conn.commit()
       elif product_type == 'appleVisionPro':
            screenSizeVison = request.form.get('screenSizeVison')
            batteryVisionPro = request.form.get('batteryVisionPro')
            dimensiones = request.form.get('dimensiones')
            sensoresVisionPro = request.form.get('sensoresVisionPro')
            modosVisionPro = request.form.get('modosVisionPro')
            juegos = request.form.get('juegos')
         # Insertar en la tabla 'appleVisionPro'
            query = """INSERT INTO appleVisionPro (productName, price, color, dimensiones, img, screenSizeVison, batteryVisionPro ,
                               sensoresVisionPro, modosVisionPro, juegos)
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (product_name, price, color, dimensiones, img, screenSizeVison, batteryVisionPro ,
                               sensoresVisionPro, modosVisionPro, juegos))
            conn.commit()
       elif product_type == 'wach':
            dimensiones = request.form.get('dimensiones')
            batteryLifeWach = request.form.get('batteryLifeWach')
            sensoresWach = request.form.get('sensoresWach')
            modos = request.form.get('modos')
         # Insertar en la tabla 'wach'
            query = """INSERT INTO applewatch (img, productName, price, color, dimensiones, batteryLifeWach, sensoresWach,
                                          modos) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (img, product_name, price, color,dimensiones, batteryLifeWach, sensoresWach,
                                modos))
            conn.commit()
            return jsonify({'status': 'success'}), 200
    except KeyError as e:
            return jsonify({'status': 'error', 'message': f'Missing field: {str(e)}'}), 400
    except Exception as e:
          return jsonify({'status': 'error', 'message': str(e)}), 500
    cursor.close()
    conn.close()
    flash({
        "message": "Producto agregado con éxito!",
        "product": {
            "id": product_id,
            "name": product_name,
            "price": price,
            "color": color,
            "img": img,
            "type": product_type
        }
    })
    
    return redirect(url_for('admin'))
    # # Retornar los detalles del producto agregado
    # message = flash(jsonify({
    #     "message": "Producto agregado con éxito!",
    #     "product": {
    #         "id": product_id,
    #         "name": product_name,
    #         "price": price,
    #         "color": color,
    #         "img": img,
    #         "type": product_type
    #     }
    # }), 200)
    # return redirect(url_for('/admin', message = message))
    


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

    # Combinar todos los productos en una sola lista
    products = mac_products + iphone_products + ipad_products + airpods_products
    print(products)

    cursor.close()
    conn.close()

    # Enviar la lista combinada a la plantilla
    return render_template('admin.html', products=products)

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
@app.route('/delete-product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = connect_db()
    cursor = conn.cursor()
    # Ajusta la tabla según el tipo de producto que corresponda
    cursor.execute("DELETE FROM mac WHERE id = %s", (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Producto eliminado con éxito!"}), 200

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