from flask import Flask, redirect, request, jsonify, render_template, url_for, flash, session, make_response
import mysql.connector
import pymysql
import mysql
import MySQLdb
import MySQLdb.cursors
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

  cursor.execute(f'''
  UPDATE {producttype} SET `producttype`= %s,`productName`= %s,`price`= %s,`color`= %s,`dimensiones`= %s,`screenSizeMac`= %s,`capacidadMac`= %s,`memoriaMac`= %s,`procesadorMac`= %s,`softwareMac`= %s,`conexionInalambricaMac`= %s,`audioMac`= %s,`tecladoMac`= %s,`camaraMac`= %s,`formatoMac`= %s,`bateriaMac`= %s WHERE id=%s
  ''', (producttype, productName, price, color, dimensiones, screenSizeMac, capacidadMac, memoriaMac, procesadorMac, softwareMac, conexionInalambricaMac, audioMac, tecladoMac, camaraMac, formatoMac, bateriaMac, product_id))
  
def updateAirpods(product_id, producttype, cursor, productName, price, color, dimensiones):
  batteryLifeAirpods = request.form.get("batteryLifeAirpods")
  noiseCancellation = request.form.get("noiseCancellation")
  sensoresAirpods = request.form.get("sensoresAirpods")
  cursor.execute(f"""
  UPDATE {producttype} SET productName=%s ,price=%s ,color=%s ,dimensiones=%s ,batteryLifeAirpods=%s ,noiseCancellation=%s ,sensoresAirpods=%s  WHERE id=%s
  """, (productName, price, color, dimensiones, batteryLifeAirpods, noiseCancellation, sensoresAirpods, product_id))
  
def updateApplewatch(product_id, producttype, cursor, productName, price, color, dimensiones):
  batteryLifeWach = request.form.get("batteryLifeWach")
  sensoresWach = request.form.get("sensoresWach")
  modos = request.form.get("modos")
  cursor.execute(f"""
  UPDATE `applewatch` SET productName=%s ,price=%s ,color=%s ,dimensiones=%s ,batteryLifeWach=%s ,sensoresWach=%s ,modos=%s  WHERE id=%s
  """,(productName, price, color, dimensiones, batteryLifeWach, sensoresWach, modos, product_id,))

def updateIpad(product_id, producttype, cursor, productName, price, color, dimensiones):
  screenSizeIpad = request.form.get("screenSizeIpad")
  capacidadIpad = request.form.get("capacidadIpad")
  memoriaipad = request.form.get("")
  procesadorIpad = request.form.get("procesadorIpad")
  camaraIpad = request.form.get("camaraIpad")
  softwareIpad = request.form.get("softwareIpad")
  conexioninalambricaIpad = request.form.get("conexioninalambricaIpad")
  audioIpad = request.form.get("audioIpad")
  geolocalizacionIpad = request.form.get("geolocalizacionIpad")
  bateriaIpad = request.form.get("bateriaIpad")
  sensoresIpad = request.form.get("sensoresIpad")
  tuchIdIpad = request.form.get("tuchIdIpad")
  siriIpad = request.form.get("siriIpad")
  cursor.execute(f"""
  UPDATE `ipad` SET productName= %s, price= %s, color= %s, dimensiones= %s, screenSizeIpad= %s, capacidadIpad= %s, memoriaipad= %s, procesadorIpad= %s, camaraIpad= %s, softwareIpad= %s, conexioninalambricaIpad= %s, audioIpad= %s, geolocalizacionIpad= %s, bateriaIpad= %s, sensoresIpad= %s, tuchIdIpad= %s, siriIpad= %s  WHERE id=%s
  """,(productName, price, color, dimensiones, screenSizeIpad, capacidadIpad, memoriaipad, procesadorIpad, camaraIpad, softwareIpad, conexioninalambricaIpad, audioIpad, geolocalizacionIpad, bateriaIpad, sensoresIpad, tuchIdIpad, siriIpad, product_id))

def updateApplevisionpro(product_id, cursor, productName, price, color, dimensiones):
  screenSizeVison = request.form.get("screenSizeVison")
  batteryVisionPro = request.form.get("batteryVisionPro")
  sensoresVisionPro = request.form.get("sensoresVisionPro")
  modosVisionPro = request.form.get("modosVisionPro")
  # juegos = request.form.get("juegos")
  juegos = int(request.form.get("juegos", 0)) if request.form.get("juegos") else None
  cursor.execute(f"""
  UPDATE `applevisionpro` SET productName=%s ,price=%s ,color=%s ,dimensiones=%s ,screenSizeVison=%s ,batteryVisionPro=%s ,sensoresVisionPro=%s ,modosVisionPro=%s ,juegos=%s  WHERE id = %s
  """, (productName, price, color, dimensiones, screenSizeVison, batteryVisionPro, sensoresVisionPro, modosVisionPro, juegos, product_id,))
  
def updatep(product_id, producttype):
  conn = connect_db()
  cursor = conn.cursor(dictionary=True)
  # Obtener datos del formulario
  productName = request.form['productName']
  # img = request.form['img']
  price = request.form['price']
  color = request.form['color']
  dimensiones = request.form.get('dimensiones')
  print(dimensiones)
  print("------------===========------------")
  print(request.form)
  print(producttype)
  if producttype == 'iphone':
    updateIphone(product_id, producttype, cursor, productName, price, color, dimensiones)
    
  elif producttype == 'mac':
    updateMac(product_id, producttype, cursor, productName, price, color, dimensiones)
    
  elif producttype == 'ipad':
    updateIpad(product_id, producttype, cursor, productName, price, color, dimensiones)
    
  elif producttype == 'airpods':
    updateAirpods(product_id, producttype, cursor, productName, price, color, dimensiones)
    
  elif producttype == 'applevisionpro':
    print("en apple vision ")
    updateApplevisionpro(product_id, cursor, productName, price, color, dimensiones)

  elif producttype == 'applewatch':
    updateApplewatch(product_id, producttype, cursor, productName, price, color, dimensiones)
  
  print("consulta exitosa")
  # Confirmar cambios en la base de datos
  conn.commit()
 