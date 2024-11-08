from flask import Flask, request, redirect, render_template, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql, re

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
            # Inicializa una lista de errores
            errors = []

            # Validar que los campos no estén vacíos
            if not nombre or not email or not direccion or not telefono or not password:
                errors.append('Todos los campos son obligatorios.')

            # Validar nombre (3-15 caracteres, solo letras)
            if len(nombre) < 3 or len(nombre) > 15 or not re.match("^[a-zA-ZÀ-ÿ]+( [a-zA-ZÀ-ÿ]+)*$", nombre):
                errors.append('Ingrese un nombre válido (solo letras, entre 3 y 15 caracteres).')

            # Validar email
            if not re.match("^[a-zA-Z0-9_]+@(gmail|hotmail)\.com$", email):
                errors.append('Ingrese un correo válido (@hotmail.com o @gmail.com).')

            # Validar dirección (mínimo 5 caracteres)
            if len(direccion) < 5 or not re.match("^[a-zA-Z0-9\s,.-]+$", direccion):
                errors.append('Ingrese una dirección válida (solo letras, números, comas y puntos).')

            # Validar teléfono (6-15 dígitos)
            if len(telefono) < 6 or len(telefono) > 15 or not re.match("^[0-9]+$", telefono):
                errors.append('Ingrese un número de teléfono válido (solo números, entre 6 y 15 dígitos).')

            # Validar contraseña
            if not re.match("^(?=.*[a-z])(?=.*[A-Z]{1})(?=.*\d{1})(?=.*[!@#$%^&*()_+[\]{};':\"\\|,.<>?`~]{1})[^\s]{6,16}$", password):
                errors.append('La contraseña debe contener una mayúscula, un número, un carácter especial, al menos una minúscula, y tener entre 6 y 16 caracteres.')

            # Si hay errores, mostrar los mensajes y volver a la plantilla
            if errors:
                for error in errors:
                    flash(error, 'error')
                return render_template('login.html', nombre=nombre, email=email, direccion=direccion, telefono=telefono)

            hashed_password = generate_password_hash(password)
            is_admin = 1 if 'admin' in email else 0
            
            conn= None

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
        print("login")
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

    @app.route('/logout', methods=['POST', 'GET'])
    def logout():
        session.pop('user_id', None)
        session.pop('is_admin', None)
        session.pop('nombre', None)
        return redirect('/index')
    # @app.route('/logout')
    # def logout():
    #     session.pop('user_id', None)
    #     session.pop('is_admin', None)
    #     return redirect('/login')
