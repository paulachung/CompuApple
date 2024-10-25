from flask import Flask, render_template, session, redirect, jsonify, url_for, request
import pymysql
import users

app = Flask(__name__)
app.secret_key = 'compu_apple'

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
        return render_template("admin.html")
    else:
        return redirect('/index')
    
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

@app.route("/insertIphone", methods=['POST', 'GET'])
def insertIphone():  
    print("en insert")  
    try:
        conn = connection()
        cursor = conn.cursor()
        
        productName = "iphone12"
        img = "https://http2.mlstatic.com/D_NQ_NP_2X_654080-MLA47781882564_102021-F.webp"
        price = 1234
        color = "blue"
        dimensiones = "10x20x2cm"
        screenSizeIphone = "3*2"
        resolutionIphone = "200px"
        resistenciaIphone = "media"
        procesadorIphone = "intel"
        camaraIphone = "doble"
        faceidIphone = "tiene"
        memoryIphone = "32gb"
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
        return jsonify({"response": "se agrego el producto a la bd correctamente"})
        # return render_template("/index")
    except Exception as e:
        return jsonify({"Response":"No se pudo insertar"})

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
