from flask import Flask, redirect, request, jsonify, render_template, url_for, flash, session, make_response
from mysql.connector import Error
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import mysql.connector
import pymysql
import os
import users
import addProduct
import updatep, verinfo
import deleteProduct
import mysql
import MySQLdb
import MySQLdb.cursors
import random
##check out carrito##
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# se guardan las imágenes subidas
UPLOAD_FOLDER = 'static/uploads/'  # Carpeta de las imágenes
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  
app.secret_key = 'compu_apple'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configuración de la conexión a la base de datos
db_config = {
    'host': '193.203.175.121',
    'user': 'u314848509_compuapple',
    'password': 'p,^.PKG2Jd!p6-F',
    'database': 'u314848509_compuapple'
}
def connection():
  # Configuración de la conexión a la base de datos
  conn = pymysql.connect(
    host= '193.203.175.121',
    user= 'u314848509_compuapple',  
    password= 'p,^.PKG2Jd!p6-F',
    # port= 3307,
    database= "u314848509_compuapple",
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

    
#eliminar producto
@app.route('/delete/<int:product_id>/<string:producttype>')
def delete_product(product_id, producttype):
    deleteProduct.delete(product_id, producttype)
    jsonify({"Response":"Producto eliminado"})
    return redirect(url_for("admin"))

# eliminar seleccionados
@app.route('/delete-selected', methods=['POST'])
def delete_selected_products():
    data = request.get_json()
    product_ids = data.get("productIds", [])
    product_types = data.get("productTypes", [])

    # Validación de los datos
    if not product_ids or not product_types or len(product_ids) != len(product_types):
        return jsonify({"status": "error", "message": "Datos incompletos"}), 400

    # Eliminar cada producto seleccionado
    for product_id, producttype in zip(product_ids, product_types):
        deleteProduct.delete(product_id, producttype)

    flash("Productos eliminados con éxito!")
    return jsonify({"status": "success", "message": "Productos eliminados correctamente"}), 200


### Ruta para actualizar un productoo existente
@app.route('/update/<int:product_id>/<string:producttype>')
def update(product_id, producttype):
    try:
        # Validar el tipo de producto
        valid_product_types = ["mac", "iphone", "airpods", "applewatch", "ipad", "applevisionpro"]
        if producttype not in valid_product_types:
            flash("Tipo de producto no válido.")
            return redirect(url_for("admin"))

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

#productos 
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
@app.route("/info/<int:product_id>/<string:producttype>")
def info(product_id, producttype):
    product = verinfo.verinfo(product_id, producttype)
    return render_template("info.html", product=product)

@app.route("/productoBuscado", methods=["GET","POST"])
def productoBuscado():
    results = []
    if request.method == 'POST':
        productoBuscado = request.form.get("productoBuscado")
        cursor = connect_db.cursor(dictionary=True)
        consulta = "SELECT * FROM productos WHERE nombre LIKE %s OR descripcion LIKE %s"
        cursor.execute(consulta, (f"%{productoBuscado}%", f"%{productoBuscado}%"))
        results = cursor.fetchall()
        cursor.close()
    return render_template("products.html", products=results)

###Productos destacados en index######
@app.route('/getFeaturedProducts', methods=['GET'])
def get_featured_products():
    try:
        # Conectar a la base de datos
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        
        # Consulta para obtener un producto de cada tipo
        query = """
            (SELECT id, img, productName, productType, price FROM mac ORDER BY RAND() LIMIT 1)
            UNION ALL
            (SELECT id, img, productName, productType, price FROM iphone ORDER BY RAND() LIMIT 1)
            UNION ALL
            (SELECT id, img, productName, productType, price FROM ipad ORDER BY RAND() LIMIT 1)
            UNION ALL
            (SELECT id, img, productName, productType, price FROM applewatch ORDER BY RAND() LIMIT 1)
            UNION ALL
            (SELECT id, img, productName, productType, price FROM applevisionpro ORDER BY RAND() LIMIT 1)
            UNION ALL
            (SELECT id, img, productName, productType, price FROM airpods ORDER BY RAND() LIMIT 1);
        """
        cursor.execute(query)
        
        # Obtener los resultados
        productos = cursor.fetchall()
        
        # Cerrar la conexión
        cursor.close()
        conn.close()
        
        # Retornar los resultados como JSON
        return jsonify(productos)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": str(err)}), 500


##############CARRITO#######################################################

#agregar al carrito

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Usuario no autenticado"}), 401

    data = request.get_json()
    product_id = data.get('productId')
    product_name = data.get('productName')
    product_price = data.get('productPrice')
    user_id = session['user_id']  # Obtén el ID del usuario desde la sesión

    if not (product_id and product_name and product_price):
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    # Conectar a la base de datos y agregar el producto al carrito
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    try:
        # Agrega el producto al carrito o incrementa la cantidad si ya existe
        cursor.execute("""
            INSERT INTO cart_items (user_id, product_id, product_name, product_price, quantity)
            VALUES (%s, %s, %s, %s, 1)
            ON DUPLICATE KEY UPDATE quantity = quantity + 1
        """, (user_id, product_id, product_name, product_price))
        conn.commit()

        return jsonify({"success": True, "message": "Producto añadido al carrito"})
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "message": "Error al agregar el producto al carrito"}), 500
    finally:
        cursor.close()
        conn.close()

##ver carrito##

@app.route('/get-cart-items', methods=['GET'])
def get_cart_items():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Usuario no autenticado"}), 401

    user_id = session['user_id']
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT product_id, product_name, product_price, quantity
            FROM cart_items
            WHERE user_id = %s
        """, (user_id,))
        cart_items = cursor.fetchall()
        return jsonify({"success": True, "cartItems": cart_items})
    except Exception as e:
        return jsonify({"success": False, "message": "Error al obtener los productos del carrito"}), 500
    finally:
        cursor.close()
        conn.close()

##check out carrito 

@app.route('/checkout', methods=['POST'])
def checkout():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Usuario no autenticado"}), 401

    user_id = session['user_id']
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    try:
        # Obtener los elementos del carrito del usuario
        cursor.execute("SELECT product_id, product_name, product_price, quantity FROM cart_items WHERE user_id = %s", (user_id,))
        cart_items = cursor.fetchall()
        
        if not cart_items:
            return jsonify({"success": False, "message": "El carrito está vacío"}), 400

        # Obtener el correo electrónico del usuario
        cursor.execute("SELECT email FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if not user:
            return jsonify({"success": False, "message": "Usuario no encontrado"}), 404

        # Enviar el correo electrónico de confirmación
        #send_confirmation_email(user['email'], cart_items)

        # Vaciar el carrito después de la compra
        cursor.execute("DELETE FROM cart_items WHERE user_id = %s", (user_id,))
        conn.commit()

        return jsonify({"success": True, "message": "Compra finalizada y correo enviado"})
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

##eliminar de a un rpoducto en el carrito 
@app.route('/remove-from-cart', methods=['POST'])
def remove_from_cart():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Usuario no autenticado"}), 401

    data = request.get_json()
    product_id = data.get('productId')

    if not product_id:
        return jsonify({"success": False, "message": "Datos inválidos"}), 400

    user_id = session['user_id']
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Eliminar el producto específico del carrito
        cursor.execute("""
            DELETE FROM cart_items
            WHERE user_id = %s AND product_id = %s
        """, (user_id, product_id))
        conn.commit()
        return jsonify({"success": True, "message": "Producto eliminado del carrito"})
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


#actualizar cantidad de producto en carrito 
@app.route('/update-cart-item', methods=['POST'])
def update_cart_item():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Usuario no autenticado"}), 401

    data = request.get_json()
    product_id = data.get('productId')
    new_quantity = data.get('newQuantity')

    if not product_id or new_quantity < 1:
        return jsonify({"success": False, "message": "Datos inválidos"}), 400

    user_id = session['user_id']
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Actualizar la cantidad del producto en el carrito
        cursor.execute("""
            UPDATE cart_items
            SET quantity = %s
            WHERE user_id = %s AND product_id = %s
        """, (new_quantity, user_id, product_id))
        conn.commit()
        return jsonify({"success": True, "message": "Cantidad actualizada"})
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        cursor.close()
        conn.close()



 ##VACIAR CARRITO
@app.route('/empty-cart', methods=['POST'])
def empty_cart():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Usuario no autenticado"}), 401

    user_id = session['user_id']
    conn = connect_db()
    cursor = conn.cursor()
    try:
        # Elimina todos los elementos del carrito del usuario
        cursor.execute("DELETE FROM cart_items WHERE user_id = %s", (user_id,))
        conn.commit()
        return jsonify({"success": True, "message": "Carrito vaciado"})
    except Exception as e:
        conn.rollback()
        return jsonify({"success": False, "message": str(e)}), 500
    finally:
        cursor.close()
        conn.close()



if __name__ == '__main__':
    app.run(debug=True) 