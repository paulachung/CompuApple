from flask import Flask, request, redirect, render_template, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql

def init_app(app, db_config):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            nombre = request.form['nombre']
            email = request.form['email']
            direccion = request.form['direccion']
            telefono = request.form['telefono']
            password = request.form['password']
            hashed_password = generate_password_hash(password)
            is_admin = 1 if email == 'admin@gmail.com' else 0

            connection = None  # Inicializar la variable connection
            cursor = None      # Inicializar la variable cursor

            try:
                connection = pymysql.connect(**db_config)
                cursor = connection.cursor()
                query = "INSERT INTO users (nombre, email, direccion, telefono, password, is_admin) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (nombre, email, direccion, telefono, hashed_password, is_admin))
                connection.commit()
                flash('Registro exitoso', 'success')
                return redirect('/login')
            except pymysql.Error as err:
                print(f"Error: {err}")
                flash('Error al registrarse. Inténtalo nuevamente.', 'error')
                return redirect('/register')
            finally:
                if cursor:  # Verifica si el cursor fue creado
                    cursor.close()
                if connection:  # Verifica si la conexión fue creada
                    connection.close()

        return render_template('login.html')  # Cambiado a la plantilla de registro

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            connection = None  # Inicializar la variable connection
            cursor = None      # Inicializar la variable cursor

            try:
                connection = pymysql.connect(**db_config)
                cursor = connection.cursor()
                query = "SELECT * FROM users WHERE email = %s"
                cursor.execute(query, (email,))
                user = cursor.fetchone()
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
            finally:
                if cursor:  # Verifica si el cursor fue creado
                    cursor.close()
                if connection:  # Verifica si la conexión fue creada
                    connection.close()

        return render_template('login.html')

    @app.route('/logout')
    def logout():
        session.pop('user_id', None)
        session.pop('is_admin', None)
        return redirect('/login')
