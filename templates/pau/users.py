# routes/users.py
from flask import Blueprint, request, redirect, render_template, session, flash, current_app
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import re

# Crear el Blueprint
users_bp = Blueprint('users', __name__)

# Configuración de la conexión a la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'compuappledb',
    'port': 3307
}

def connection():
    return pymysql.connect(**db_config, cursorclass=pymysql.cursors.DictCursor)

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        email = request.form['email'].strip()
        direccion = request.form['direccion'].strip()
        telefono = request.form['telefono'].strip()
        password = request.form['password'].strip()

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

        try:
            conn = connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO users (nombre, email, direccion, telefono, password, is_admin)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nombre, email, direccion, telefono, hashed_password, is_admin))
            conn.commit()
            flash('Registro exitoso', 'success')
            return redirect('/login')
        except Exception as err:
            print(f"Error: {err}")
            flash('Error al registrarse. Inténtalo nuevamente.', 'error')
            return render_template('login.html', nombre=nombre, email=email, direccion=direccion, telefono=telefono)
        finally:
            if conn:
                conn.close()

    return render_template('login.html')



@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            conn = connection()
            cursor = conn.cursor()
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
            
        except Exception as err:
            print(f"Error: {err}")
            flash('Error al iniciar sesión. Inténtalo de nuevo.', 'error')
            return redirect('/login')
        finally:
            if conn:
                conn.close()

    return render_template('login.html')

@users_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    session.pop('is_admin', None)
    session.pop('nombre', None)
    return redirect('/index')
