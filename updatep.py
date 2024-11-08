from flask import Flask, redirect, request, jsonify, render_template, url_for, flash, session, make_response
import mysql.connector
import pymysql
import mysql
import MySQLdb
import MySQLdb.cursors
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
  
def updateIphone(product_id, producttype, cursor, productName, price, color, dimensiones):
  screenSizeIphone = request.form['screenSizeIphone']
  resolutionIphone = request.form['resolutionIphone']
  resistenciaIphone = request.form['resistenciaIphone']
  procesadorIphone = request.form['procesadorIphone']
  camaraIphone = request.form['camaraIphone']
  faceidIphone = request.form['faceidIphone']
  memoryIphone = request.form['memoryIphone']
  geolocalizacion = request.form['geolocalizacion']
  reproduccionIphone = request.form['reproduccionIphone']
  sensoresIphone = request.form['sensoresIphone']
  grabacionIphone = request.form['grabacionIphone']
  siriIphone = request.form['siriIphone']
  bateriaIphone = request.form['bateriaIphone']

  cursor.execute(f'''
  UPDATE {producttype} SET  `productName`=%s, `price`=%s, `color`=%s, `dimensiones`=%s, 
  `screenSizeIphone`=%s, `resolutionIphone`=%s, `resistenciaIphone`=%s, `procesadorIphone`=%s, 
  `camaraIphone`=%s, `faceidIphone`=%s, `memoryIphone`=%s, `geolocalizacion`=%s, 
  `reproduccionIphone`=%s, `sensoresIphone`=%s, `grabacionIphone`=%s, `siriIphone`=%s, 
  `bateriaIphone`=%s WHERE id=%s
''', ( productName, price, color, dimensiones, screenSizeIphone, resolutionIphone, resistenciaIphone, 
      procesadorIphone, camaraIphone, faceidIphone, memoryIphone, geolocalizacion, reproduccionIphone, 
      sensoresIphone, grabacionIphone, siriIphone, bateriaIphone, product_id))
  
def updateMac(product_id, producttype, cursor, productName, price, color, dimensiones):
  # dimensiones = request.form['dimensiones'] 
  screenSizeMac = request.form['screenSizeMac'] 
  capacidadMac = request.form['capacidadMac'] 
  memoriaMac = request.form['memoriaMac'] 
  procesadorMac = request.form['procesadorMac'] 
  softwareMac = request.form['softwareMac'] 
  conexionInalambricaMac = request.form['conexionInalambricaMac'] 
  audioMac = request.form['audioMac'] 
  tecladoMac = request.form['tecladoMac'] 
  camaraMac = request.form['camaraMac'] 
  formatoMac = request.form['formatoMac'] 
  bateriaMac = request.form['bateriaMac'] 

  cursor.execute(f'''
  UPDATE {producttype} SET `producttype`= %s,`productName`= %s,`price`= %s,`color`= %s,`dimensiones`= %s,`screenSizeMac`= %s,`capacidadMac`= %s,`memoriaMac`= %s,`procesadorMac`= %s,`softwareMac`= %s,`conexionInalambricaMac`= %s,`audioMac`= %s,`tecladoMac`= %s,`camaraMac`= %s,`formatoMac`= %s,`bateriaMac`= %s WHERE id=%s
  ''', (producttype, productName, price, color, dimensiones, screenSizeMac, capacidadMac, memoriaMac, procesadorMac, softwareMac, conexionInalambricaMac, audioMac, tecladoMac, camaraMac, formatoMac, bateriaMac, product_id))
  
def updatep(product_id, producttype):
  conn = connect_db()
  cursor = conn.cursor(dictionary=True)
  # Obtener datos del formulario
  productName = request.form['productName']
  # img = request.form['img']
  price = request.form['price']
  color = request.form['color']
  dimensiones = request.form['dimensiones']
  
  if producttype == 'iphone':
    updateIphone(product_id, producttype, cursor, productName, price, color, dimensiones)
    
  elif producttype == 'mac':
    updateMac(product_id, producttype, cursor, productName, price, color, dimensiones)
    
  elif producttype == 'ipad':
    updateIphone(product_id, producttype, cursor, productName, price, color, dimensiones)
    
  elif producttype == 'airpods':
    updateIphone(product_id, producttype, cursor, productName, price, color, dimensiones)
    
  elif producttype == 'appleVisionPro':
    updateIphone(product_id, producttype, cursor, productName, price, color, dimensiones)

  elif producttype == 'applewatch':
    updateIphone(product_id, producttype, cursor, productName, price, color, dimensiones)
  
  print("consulta exitosa")
  # Confirmar cambios en la base de datos
  conn.commit()
  flash("Se modificó con éxito")
  print("Se modificó con éxito")