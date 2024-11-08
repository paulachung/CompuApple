from flask import Flask, render_template, session, redirect, jsonify, url_for, request, session as se
import pymysql
import users
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
# Inicializar el módulo de usuarios y pasar la configuración de la DB
users.init_app(app, db_config)

@app.route('/')
def home():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/products', methods=["GET"])
def products():
    return selectIphones()

@app.route('/aboutUs')
def about_us():
    return render_template('aboutUs.html')

@app.route('/admin', methods=["POST","GET"])
def admin():
    if 'is_admin' in session and session['is_admin']:
        # print("metodo", request.method)
        # if request.method == "POST":
        #     print("antes de insert")
        #     return insertIphone()
        # return redirect(url_for("insertIphone"))
        se["user"] = session['is_admin']
        return render_template("admin.html")
    else:
        return redirect('/index')
@app.route("/selectByIdIphone/<int:id>", methods=["GET"])
def selectByIdIphone(id):
    try:
        conn = connection()
        cursor = conn.cursor()
        
        query="SELECT `id`, `img`, `productName`, `price`, `color`, `dimensiones`, `screenSizeIphone`, `resolutionIphone`, `resistenciaIphone`, `procesadorIphone`, `camaraIphone`, `faceidIphone`, `memoryIphone`, `geolocalizacion`, `reproduccionIphone`, `sensoresIphone`, `grabacionIphone`, `siriIphone`, `bateriaIphone` FROM `iphone` WHERE id=%s"
        iphone = cursor.fetchone()
        cursor.execute(query, (id,)) 
        
        cursor.close()
        conn.close()
        # return render_template('products.html', data=iphones)
        return jsonify({"error": iphone})
        
    except Exception as e:
        print("error en la coneccion",e)
        return jsonify({"error": "Error en la conexión o en la operación"}), 500
    
@app.route("/selectIphones", methods=["GET"])
def selectIphones():
    try:
        conn = connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT `id`, `img`, `productName`, `price`, `color`, `dimensiones`, `screenSizeIphone`, `resolutionIphone`, `resistenciaIphone`, `procesadorIphone`, `camaraIphone`, `faceidIphone`, `memoryIphone`, `geolocalizacion`, `reproduccionIphone`, `sensoresIphone`, `grabacionIphone`, `siriIphone`, `bateriaIphone` FROM `iphone`")
        iphones = cursor.fetchall()
        print(iphones)     
        
        cursor.close()
        conn.close()
        # return render_template('products.html', data=iphones)
        return jsonify({"error": iphones})
        
    except Exception as e:
        print("error en la coneccion",e)
        return jsonify({"error": "Error en la conexión o en la operación"}), 500

@app.route("/insertIphone", methods=['POST'])
def insertIphone():  
    print(request.form)
    try:
        conn = connection()
        cursor = conn.cursor()
        productType = request.form['productType']
        print(f"Tipo de producto seleccionado: {productType}")
        
        productName = request.form['productName']
          
        if productType == 'mac':
            print("mac")
            '''screen_size_mac = request.form.get('screenSizeMac')
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
        '''
        elif productType == 'iphone':
            try:
                # productName = "Iphone 20"
                img = "ruta_de_la_imagen"
                price = "asd"
                color = "blue"
                dimensiones = "10x20x2cm"
                screenSizeIphone = "3*2"
                resolutionIphone = "200px"
                resistenciaIphone = "media"
                procesadorIphone = "intel"
                camaraIphone = "doble"
                faceidIphone = "tiene"
                memoryIphone = "200gb"
                geolocalizacion = "no"
                reproduccionIphone = "4k"
                sensoresIphone = "id face y huella dactilar"
                grabacionIphone = "HD"
                siriIphone = "incluye"
                bateriaIphone = "4hs"
                query = "INSERT INTO `iphone`(`productName`, img, `price`, `color`, `dimensiones`,`screenSizeIphone`, `resolutionIphone`, `resistenciaIphone`, `procesadorIphone`, `camaraIphone`, `faceidIphone`, `memoryIphone`, `geolocalizacion`, `reproduccionIphone`, `sensoresIphone`, `grabacionIphone`, `siriIphone`, `bateriaIphone`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
                cursor.execute(query, (productName, img, price, color, dimensiones,screenSizeIphone, resolutionIphone, resistenciaIphone, procesadorIphone, camaraIphone, faceidIphone, memoryIphone, geolocalizacion, reproduccionIphone, sensoresIphone, grabacionIphone, siriIphone, bateriaIphone))

                conn.commit()
                cursor.close()
                conn.close()
                return jsonify({"message": "Producto agregado con éxito!"}), 200
            except Exception as e:
                print(e)
                return jsonify({"Error": "no se pudo agrego el producto a la bd correctamente"})                
        ''' screen_size_iphone = request.form.get('screenSizeIphone')
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
            
        elif productType == 'ipad':
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
        elif productType == 'airpods':
            batteryLifeAirpods = request.form.get('batteryLifeAirpods')
            noiseCancellation = request.form.get('noiseCancellation')
            sensoresAirpods = request.form.get('sensoresAirpods')
            
            # Insertar en la tabla 'airpods'
            query = """INSERT INTO airpods (productName, price, color, img, batteryLifeAirpods, noiseCancellation,
                                sensoresAirpods) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (product_name, price, color, img, batteryLifeAirpods, noiseCancellation,
                                sensoresAirpods))
        elif productType == 'appleVisionPro':
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
        elif productType == 'wach':
            batteryLifeWach = request.form.get('batteryLifeWach')
            sensoresWach = request.form.get('sensoresWach')
            sistemasOperativosWach = request.form.get('sistemasOperativosWach')
            materialWach = request.form.get('materialWach')
            # Insertar en la tabla 'wach'
            query = """INSERT INTO wach (productName, price, color, img, batteryLifeWach, sensoresWach,
                                sistemasOperativosWach, materialWach) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (product_name, price, color, img, batteryLifeWach, sensoresWach,
                                sistemasOperativosWach, materialWach))'''

    except Exception as e:
        print(e)
        return jsonify({"Un error": "ocurrio " + e})

@app.route("/updateIphone/<int:id>", methods=["PUT","GET"])
def updateIphone(id):
    try:
        conn = connection()
        cursor = conn.cursor()
        try:
            productName = "Iphone 20"
            price = "asd"
            color = "blue"
            dimensiones = "10x20x2cm"
            screenSizeIphone = "3*2"
            resolutionIphone = "200px"
            resistenciaIphone = "media"
            procesadorIphone = "intel"
            camaraIphone = "doble"
            faceidIphone = "tiene"
            memoryIphone = "200gb"
            geolocalizacion = "no"
            reproduccionIphone = "4k"
            sensoresIphone = "id face y huella dactilar"
            grabacionIphone = "HD"
            siriIphone = "incluye"
            bateriaIphone = "4hs"
            
            query = """
            UPDATE `iphone` 
            SET `productName`=%s, `price`=%s, `color`=%s, `dimensiones`=%s, `screenSizeIphone`=%s, 
            `resolutionIphone`=%s, `resistenciaIphone`=%s, `procesadorIphone`=%s, `camaraIphone`=%s, 
            `faceidIphone`=%s, `memoryIphone`=%s, `geolocalizacion`=%s, `reproduccionIphone`=%s, 
            `sensoresIphone`=%s, `grabacionIphone`=%s, `siriIphone`=%s, `bateriaIphone`=%s 
            WHERE id=%s
            """
            cursor.execute(query,(productName, price, color, dimensiones, screenSizeIphone, resolutionIphone, resistenciaIphone, procesadorIphone, camaraIphone, faceidIphone, memoryIphone, geolocalizacion, reproduccionIphone, sensoresIphone, grabacionIphone, siriIphone, bateriaIphone, id))
            
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"Response":"Se actualizo correctamente"})
        except Exception as e:
            return jsonify({"Fallo la actualización":str(e)})
    except Exception as e:
        return jsonify({"Fallo la conexión": str(e)}), 500
    
@app.route("/deleteIphone/<int:id>",methods=["POST","GET"])
def deleteIphone(id):
    try:
        conn = connection()
        cursor = conn.cursor()
        # Verificar si existe un registro con el id proporcionado
        cursor.execute("SELECT * FROM `iphone` WHERE id = %s", (id,))
        record = cursor.fetchone()
        
        if record:
            # Si el registro existe, eliminarlo
            query = "DELETE FROM `iphone` WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()

            response = jsonify({"Response": "Se eliminó correctamente"})
        else:
            # Si no existe, retornar un mensaje adecuado
            response = jsonify({"Response": "No existe un producto con ese id en la base de datos"})

        cursor.close()
        conn.close()
        return response
    except Exception as e:
        return jsonify({"Fallo la conexión": str(e)}), 500
        

if __name__ == '__main__':
    app.run(debug=True)
