from flask import Flask, redirect, request, jsonify, render_template, url_for, flash
import mysql.connector
import pymysql

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

def delete(app, product_id):
  try:
      conn = connect_db()
      cursor = conn.cursor()
      # return jsonify({"message": "Producto eliminado con éxito!"}), 200

      product_type = request.args.get('productType')
      try:
          # Insertar datos según el tipo de producto seleccionado
          if product_type == 'mac':
              cursor.execute("DELETE FROM mac WHERE id = %s", (product_id,))
              conn.commit()
              
          elif product_type == 'iphone':
              cursor.execute("DELETE FROM iphone WHERE id = %s", (product_id,))
              conn.commit()
                              
          elif product_type == 'ipad':
              cursor.execute("DELETE FROM ipad WHERE id = %s", (product_id,))
              conn.commit()
              
          elif product_type == 'airpods':
              cursor.execute("DELETE FROM airpods WHERE id = %s", (product_id,))
              conn.commit()
              
          elif product_type == 'appleVisionPro':
              cursor.execute("DELETE FROM applevisionpro WHERE id = %s", (product_id,))
              conn.commit()
              
          elif product_type == 'wach':
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