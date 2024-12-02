from flask import Flask, request, redirect, render_template, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql, re

def validate_user_input(email, password):
    errors = []

    # Validar email
    if not re.match(r"^[a-zA-Z0-9_]+@(gmail|hotmail)\.com$", email):
        errors.append('Ingrese un correo válido (@hotmail.com o @gmail.com).')

    # Validar contraseña
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z]{1})(?=.*\d{1})(?=.*[!@#$%^&*()_+[\]{};':\"\\|,.<>?`~]{1})[^\s]{6,16}$", password):
        errors.append('La contraseña debe contener una mayúscula, un número, un carácter especial, al menos una minúscula, y tener entre 6 y 16 caracteres.')

    return errors

def init_app(app, db_config):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            nombre = request.form['nombre'].strip()
            email = request.form['email'].strip()
            direccion = request.form['direccion'].strip()
            telefono = request.form['telefono'].strip()
            password = request.form['password'].strip()

            errors = []

            # Validaciones específicas de registro
            if not nombre or not direccion or not telefono:
                errors.append('Todos los campos son obligatorios.')

            if len(nombre) < 3 or len(nombre) > 15 or not re.match("^[a-zA-ZÀ-ÿ]+( [a-zA-ZÀ-ÿ]+)*$", nombre):
                errors.append('Ingrese un nombre válido (solo letras, entre 3 y 15 caracteres).')

            if len(direccion) < 5 or not re.match(r"^[a-zA-Z0-9\s,.-]+$", direccion):
                errors.append('Ingrese una dirección válida (solo letras, números, comas y puntos).')

            if len(telefono) < 6 or len(telefono) > 15 or not re.match("^[0-9]+$", telefono):
                errors.append('Ingrese un número de teléfono válido (solo números, entre 6 y 15 dígitos).')

            # Validaciones de email y password (reutilizadas)
            errors += validate_user_input(email, password)

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

                # Verificar si ya existe un administrador en la base de datos
                cursor.execute("SELECT COUNT(*) FROM users WHERE is_admin = 1")
                admin_count = cursor.fetchone()[0]

                # Asigna el rol de administrador solo si no existe otro
                is_admin = 1 if 'admin' in email.lower() and admin_count == 0 else 0

                # Insertar el nuevo usuario en la base de datos
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
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()

        return render_template('login.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        print("login")
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            
            # Validaciones de email y password
            errors = validate_user_input(email, password)

            connection = None  # Inicializar la variable connection
            cursor = None      # Inicializar la variable cursor
            
            if errors:
                for error in errors:
                    flash(error, 'error')
                return redirect('/login')

            try:
                connection = pymysql.connect(**db_config)
                cursor = connection.cursor(pymysql.cursors.DictCursor)
                query = "SELECT * FROM users WHERE email = %s"
                cursor.execute(query, (email,))
                user = cursor.fetchone()
                if not user or not check_password_hash(user['password'], password):
                    flash('El usuario o contraseña son incorrectos', 'error')
                    return redirect('/login')
                # Si el inicio de sesión es exitoso
                session['user_id'] = user['id']
                session['nombre'] = user['nombre']
                session['is_admin'] = user['is_admin']
                return redirect('/admin' if user['is_admin'] else '/index')
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

