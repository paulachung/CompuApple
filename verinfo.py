from flask import jsonify, flash, render_template
import mysql.connector
import pymysql

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
  )
  return conn
# Conectar a la base de datos
def connect_db():
  return mysql.connector.connect(**db_config)  

def verinfo(product_id, producttype):
  print("en ver info ", product_id ,  ' ' , producttype)
  try:
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    # return jsonify({"message": "Producto eliminado con éxito!"}), 200
    #   product_type = request.args.get('productType')
    try:
        print(producttype)
        if producttype == 'mac':
          cursor.execute("SELECT * FROM mac WHERE id = %s", (product_id,))
          mac = cursor.fetchone()
          return mac
            
        elif producttype == 'iphone':
          cursor.execute("SELECT * FROM iphone WHERE id = %s", (product_id,))
          product = cursor.fetchone()
          return product
                            
        elif producttype == 'ipad':
          cursor.execute("SELECT * FROM ipad WHERE id = %s", (product_id,))
          product = cursor.fetchone()
          return product
            
        elif producttype == 'airpods':
          cursor.execute("SELECT * FROM airpods WHERE id = %s", (product_id,))
          product = cursor.fetchone()
          return product
            
        elif producttype == 'applevisionpro':
          cursor.execute("SELECT * FROM applevisionpro WHERE id = %s", (product_id,))
          product = cursor.fetchone()
          return product
            
        elif producttype == 'applewatch':
          cursor.execute("SELECT * FROM applewatch WHERE id = %s", (product_id,))
          product = cursor.fetchone()
          print("product: ",product)
          return product
            
        cursor.close()
        conn.close()
        return flash( "Producto eliminado con éxito!")

        # return jsonify({'status': 'success, se borro el producto correctamente!'}), 200
    except KeyError as e:
            return jsonify({'status': 'error', 'message': f'Falta el campo: {str(e)}'}), 400
    except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

  except Exception as e:
        return jsonify({"message": "Error al ver detalles del producto, no se pudo mostrar"}), 422