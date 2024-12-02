from flask import jsonify, flash
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

def delete(product_id, producttype):
  try:
      conn = connect_db()
      cursor = conn.cursor()
      # return jsonify({"message": "Producto eliminado con éxito!"}), 200
      #   product_type = request.args.get('productType')
      try:
          # Insertar datos según el tipo de producto seleccionado
          if producttype == 'mac':
              cursor.execute("DELETE FROM mac WHERE id = %s", (product_id,))
              conn.commit()
              
          elif producttype == 'iphone':
              cursor.execute("DELETE FROM iphone WHERE id = %s", (product_id,))
              conn.commit()
                              
          elif producttype == 'ipad':
              cursor.execute("DELETE FROM ipad WHERE id = %s", (product_id,))
              conn.commit()
              
          elif producttype == 'airpods':
              cursor.execute("DELETE FROM airpods WHERE id = %s", (product_id,))
              conn.commit()
              
          elif producttype == 'applevisionpro':
              cursor.execute("DELETE FROM applevisionpro WHERE id = %s", (product_id,))
              conn.commit()
              
          elif producttype == 'applewatch':
              cursor.execute("DELETE FROM applewatch WHERE id = %s", (product_id,))
              conn.commit()
              
          cursor.close()
          conn.close()
          return flash( "Producto eliminado con éxito!")

          # return jsonify({'status': 'success, se borro el producto correctamente!'}), 200
      except KeyError as e:
              return jsonify({'status': 'error', 'message': f'Missing field: {str(e)}'}), 400
      except Exception as e:
              return jsonify({'status': 'error', 'message': str(e)}), 500

  except Exception as e:
        return jsonify({"message": "Error al eliminar, no se pudo eliminar"}), 422