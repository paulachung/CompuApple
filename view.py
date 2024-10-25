from flask import Flask, request, redirect, render_template, jsonify, url_for
# import mysql.connector
import os
import pymysql

app = Flask(__name__)
@app.route('/admin', methods=['GET'])
def admin(): 
    # Renderizar la página HTML del administrador
    return render_template('admin.html')