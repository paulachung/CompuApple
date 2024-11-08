from flask import Flask, redirect, request, jsonify, render_template
import mysql.connector
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define la carpeta donde se guardarán las imágenes subidas
UPLOAD_FOLDER = 'static/uploads/'  # Carpeta de las imágenes
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Asegúrate de usar la variable aquí
app.secret_key = 'compu_apple'

# Crea la carpeta de uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'compuappledb',
    'port': 3307
}

# Conectar a la base de datos
def connect_db():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return redirect('/admin')

# Ruta para la página principal (admin)
@app.route('/admin')
def admin_page():
    return render_template('admin.html')

# Agregar un nuevo producto
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

    # Aquí utilizamos img_path en lugar de img
    img = img_path

    # Insertar datos según el tipo de producto seleccionado
    if product_type == 'mac':
        screen_size_mac = request.form.get('screenSizeMac')
        capacidad_mac = request.form.get('capacidadMac')
        memoria_mac = request.form.get('memoriaMac')
        procesador_mac = request.form.get('procesadorMac')
        software_mac = request.form.get('softwareMac')
        conexion_inalambrica_mac = request.form.get('conexionInalambricaMac')
        audio_mac = request.form.get('audioMac')
        teclado_mac = request.form.get('tecladoMac')
        camara_mac = request.form.get('camaraMac')
        formato_video_mac = request.form.get('formatoMac')
        bateria_mac = request.form.get('bateriaMac')

        # Insertar en la tabla 'mac'
        query = """INSERT INTO mac (productName, price, color, img,
                               screen_size_mac, capacidad_mac, memoria_mac, procesador_mac, software_mac, 
                               conexion_inalambrica_mac, audio_mac, teclado_mac, camara_mac, formato_video_mac, bateria_mac) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (product_name, price, color, img,
                               screen_size_mac, capacidad_mac, memoria_mac, procesador_mac, software_mac, 
                               conexion_inalambrica_mac, audio_mac, teclado_mac, camara_mac, formato_video_mac, bateria_mac))

    elif product_type == 'iphone':
        screen_size_iphone = request.form.get('screenSizeIphone')
        resolution_iphone = request.form.get('resolutionIphone')
        resistencia_iphone = request.form.get('resistenciaIphone')
        procesador_iphone = request.form.get('procesadorIphone')
        camara_iphone = request.form.get('camaraIphone')
        faceid_iphone = request.form.get('faceidIphone')
        memory_iphone = request.form.get('memoryIphone')
        geolocalizacion = request.form.get('geolocalizacion')
        reproduccion_iphone = request.form.get('reproduccionIphone')
        sensores_iphone = request.form.get('sensoresIphone')
        grabacion_iphone = request.form.get('grabacionIphone')
        siri_iphone = request.form.get('siriIphone')
        bateria_iphone = request.form.get('bateriaIphone')

        # Insertar en la tabla 'iphone'
        query = """INSERT INTO iphone (productName, price, color, img,
                               screen_size_iphone, resolution_iphone, resistencia_iphone, procesador_iphone, 
                               camara_iphone, faceid_iphone, memory_iphone, geolocalizacion, reproduccion_iphone, 
                               sensores_iphone, grabacion_iphone, siri_iphone, bateria_iphone) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (product_name, price, color, img,
                               screen_size_iphone, resolution_iphone, resistencia_iphone, procesador_iphone, 
                               camara_iphone, faceid_iphone, memory_iphone, geolocalizacion, reproduccion_iphone, 
                               sensores_iphone, grabacion_iphone, siri_iphone, bateria_iphone))
        
    elif product_type == 'ipad':
        screen_size_ipad = request.form.get('screenSizeIpad')
        capacidad_ipad = request.form.get('capacidadIpad')
        memoria_ipad = request.form.get('memoriaipad')
        procesador_ipad = request.form.get('procesadorIpad')
        camara_ipad = request.form.get('camaraIpad')
        software_ipad = request.form.get('softwareIpad')
        conexion_inalambrica_ipad = request.form.get('conexioninalambricaIpad')
        audio_ipad = request.form.get('audioIpad')
        geolocalizacion_ipad = request.form.get('geolocalizacionIpad')
        bateria_ipad = request.form.get('bateriaIpad')
        sensores_ipad = request.form.get('sensoresIpad')
        tuch_id_ipad = request.form.get('tuchIdIpad')
        siri_ipad = request.form.get('siriIpad')

        # Insertar en la tabla 'ipad'
        query = """INSERT INTO ipad (productName, price, color, img,
                               screen_size_ipad, capacidad_ipad, memoria_ipad, procesador_ipad, camara_ipad, 
                               software_ipad, conexion_inalambrica_ipad, audio_ipad, geolocalizacion_ipad, 
                               bateria_ipad, sensores_ipad, tuch_id_ipad, siri_ipad) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (product_name, price, color, img,
                               screen_size_ipad, capacidad_ipad, memoria_ipad, procesador_ipad, camara_ipad, 
                               software_ipad, conexion_inalambrica_ipad, audio_ipad, geolocalizacion_ipad, 
                               bateria_ipad, sensores_ipad, tuch_id_ipad, siri_ipad))
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
    elif product_type == 'appleVisionPro':
         screenSizeVison = request.form.get('screenSizeVison')
         batteryVisionPro = request.form.get('batteryVisionPro')
         sensoresVisionPro = request.form.get('sensoresVisionPro')
         modosVisionPro = request.form.get('modosVisionPro')
         juegos = request.form.get('juegos')
         # Insertar en la tabla 'appleVisionPro'
         query = """INSERT INTO appleVisionPro (productName, price, color, img, screenSizeVison, batteryVisionPro ,
                               sensoresVisionPro, modosVisionPro, juegos)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
         cursor.execute(query, (product_name, price, color, img, screenSizeVison, batteryVisionPro ,
                               sensoresVisionPro, modosVisionPro, juegos))
    elif product_type == 'wach':
         batteryLifeWach = request.form.get('batteryLifeWach')
         sensoresWach = request.form.get('sensoresWach')
         sistemasOperativosWach = request.form.get('sistemasOperativosWach')
         materialWach = request.form.get('materialWach')
         # Insertar en la tabla 'wach'
         query = """INSERT INTO wach (productName, price, color, img, batteryLifeWach, sensoresWach,
                               sistemasOperativosWach, materialWach) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
         cursor.execute(query, (product_name, price, color, img, batteryLifeWach, sensoresWach,
                               sistemasOperativosWach, materialWach))
         
    # Confirma los cambios en la base de datos
    conn.commit()
    return jsonify({"message": "Producto agregado con éxito!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
