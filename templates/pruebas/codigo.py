# if 'img' not in request.files:
#     return jsonify({"error": "No file part"}), 400
# img_file = request.files['img']
# if img_file.filename == '':
#     return jsonify({"error": "No selected file"}), 400



# Guardar la imagen en la carpeta de uploads
# filename = secure_filename(img_file.filename)
# img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# img_file.save(img_path)


# productType = request.form['productType']  # Tipo de producto
# price = request.form['price']  # Precio del producto
# color = request.form['color']  # Color del producto

# Aquí utilizamos img_path en lugar de img
# img = img_path


#     cursor.execute(query, (productName, img, price, color, dimensiones,screenSizeIphone, resolutionIphone, resistenciaIphone, procesadorIphone, camaraIphone, faceidIphone, memoryIphone, geolocalizacion, reproduccionIphone, sensoresIphone, grabacionIphone, siriIphone, bateriaIphone))
            
#     conn.commit()
#     return jsonify({"response": "se agrego el producto a la bd correctamente"})
#     # return render_template("/index")
# except Exception as e:
#     return jsonify({"Response":"No se pudo insertar"})