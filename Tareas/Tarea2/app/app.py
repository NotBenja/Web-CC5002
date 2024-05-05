from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import validate_login_user, validate_register_user, validate_confession
from db import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ver-productos')
def ver_productos():
    return render_template('productos/ver-productos.html')

@app.route('/agregar-producto')
def agregar_producto():
    # Lógica para agregar un producto
    return render_template('productos/agregar-producto.html')

@app.route('/agregar-pedido')
def agregar_pedido():
    # Lógica para agregar un pedido
    return render_template('pedidos/agregar-pedido.html')

@app.route('/ver-pedidos')
def ver_pedidos():
    # Lógica para ver los pedidos
    return render_template('pedidos/ver-pedidos.html')

if __name__ == "__main__":
    app.run(debug=True)