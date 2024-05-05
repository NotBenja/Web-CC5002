from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import validate_login_user, validate_register_user, validate_confession
from db import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/agregar-producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        # Hacer validaciones aquí
        # Agregar producto a la base de datos aquí
        return redirect(url_for("index"))
    elif request.method == 'GET':
        return render_template('productos/agregar-producto.html')
    
@app.route('/ver-productos')
def ver_productos():
    return render_template('productos/ver-productos.html')    

@app.route('/agregar-pedido', methods=['GET', 'POST'])
def agregar_pedido():
    if request.method == 'POST':
        # Hacer validaciones aquí
        # Agregar producto a la base de datos aquí
        return redirect(url_for("index"))
    elif request.method == 'GET':
        return render_template('pedidos/agregar-pedido.html')

@app.route('/ver-pedidos')
def ver_pedidos():
    # Lógica para ver los pedidos
    return render_template('pedidos/ver-pedidos.html')

@app.route('/informacion-pedido')
def informacion_pedido():
    return render_template('pedidos/informacion-pedido.html')

@app.route('/informacion-producto')
def informacion_producto():
    return render_template('productos/informacion-producto.html')

if __name__ == "__main__":
    app.run(debug=True)