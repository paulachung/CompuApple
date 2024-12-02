from flask import redirect, request, jsonify, render_template, url_for, flash
from werkzeug.utils import secure_filename
import pymysql, mysql
import os
# Configuración de la conexión a la base de datos
db_config = {
    'host': '193.203.175.121',
    'user': 'u314848509_compuapple',
    'password': 'p,^.PKG2Jd!p6-F',
    'database': 'u314848509_compuapple',
}
def connection():
  # Configuración de la conexión a la base de datos
  conn = pymysql.connect(
      host= '193.203.175.121',
    user= 'u314848509_compuapple',  
    password= 'p,^.PKG2Jd!p6-F',
    # port= 3307,
    database= "u314848509_compuapple"
  )
  return conn
# Conectar a la base de datos
def connect_db():
    return mysql.connector.connect(**db_config)
  
from flask import Flask, request, jsonify, flash
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def addProduct(app):
    print("en add")
    conn = connect_db()
    cursor = conn.cursor()

    if 'img' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    img_file = request.files['img']
    
    if img_file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Verificar si el archivo tiene una extensión permitida
    if not allowed_file(img_file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    # Guardar la imagen en la carpeta de uploads
    filename = secure_filename(img_file.filename)
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img_file.save(img_path)

    # Recibir datos del formulario
    product_type = request.form['productType']  # Tipo de producto
    product_name = request.form['productName']  # Nombre del producto
    price = request.form['price']  # Precio del producto
    color = request.form['color']  # Color del producto

    # img_path en lugar de img
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
      elif product_type == 'applevisionpro':
          screenSizeVison = request.form.get('screenSizeVison')
          batteryVisionPro = request.form.get('batteryVisionPro')
          dimensiones = request.form.get('dimensiones')
          sensoresVisionPro = request.form.get('sensoresVisionPro')
          modosVisionPro = request.form.get('modosVisionPro')
          juegos = request.form.get('juegos')
        # Insertar en la tabla 'appleVisionPro'
          query = """INSERT INTO applevisionpro (productName, price, color, dimensiones, img, screenSizeVison, batteryVisionPro ,
                              sensoresVisionPro, modosVisionPro, juegos)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
          cursor.execute(query, (product_name, price, color, dimensiones, img, screenSizeVison, batteryVisionPro ,
                              sensoresVisionPro, modosVisionPro, juegos))
          conn.commit()
      elif product_type == 'applewatch':
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
    finally:
        cursor.close()
        conn.close()

    print("se agrego")
    flash("Producto agregado con éxito!")

  
  
  
  

