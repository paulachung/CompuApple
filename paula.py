from flask import Flask, request, redirect, render_template, jsonify, url_for, flash, generate_password_hash, session, check_password_hash
import os
import pymysql

app = Flask(__name__)
conn = pymysql.connect(
    host= 'localhost',
    user= 'root',  
    password= '',  
    database= "compuapple"
)
db_config = {
  "host":"localhost",
  "user":"root",
  "password":"",
  "database":"compuapple"
}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # obtener datos del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        password = request.form['password']
        
        # hash contraseña
        hashed_password = generate_password_hash(password)

        try:
            connection = pymysql.connect(**db_config)
            cursor = connection.cursor()
            query = "INSERT INTO users (nombre, email, direccion, telefono, password) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (nombre, email, direccion, telefono, hashed_password))
            connection.commit()
            cursor.close()
            connection.close()
            flash('Registro exitoso', 'success')
            return redirect('/login')  # Redirige al inicio de sesión
        except pymysql.Error as err:
            print(f"Error: {err}")
            flash('Error al registrarse. Inténtalo nuevamente.', 'error')
            return redirect('/register')

    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            connection = pymysql.connect(**db_config)
            cursor = connection.cursor()
            query = "SELECT * FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            cursor.close()
            connection.close()

            if user and check_password_hash(user[5], password):
                session['user_id'] = user[0]  
                session['is_admin'] = user[6]  
                return redirect('/admin' if user[6] else '/index') 
            else:
                flash('Correo o contraseña incorrectos.', 'error')
                return redirect('/login')
        except pymysql.Error as err:
            print(f"Error: {err}")
            flash('Error al iniciar sesión. Inténtalo de nuevo.', 'error')
            return redirect('/login')

    return render_template('login.html')

@app.route('/admin')
def admin():
    if 'is_admin' in session and session['is_admin']:
        return render_template('admin.html')
    else:
        return redirect('/index')