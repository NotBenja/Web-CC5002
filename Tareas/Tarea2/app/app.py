from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import validate_add_product
from db import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os

UPLOAD_FOLDER = 'static/uploads'
ORDER_FOLDER = 'pedidos'
PRODUCT_FOLDER = 'productos'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000 # 16 MB

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File exceeds the maximum file size allowed', 413

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/agregar-producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        # Obtenemos los productos con sus tipos
        tiposProducto = []
        productos = []
        for i in range(1,6):
            tipo = request.form.get(f'tipoProducto{i}')
            producto = request.form.get(f'producto{i}')
            if tipo and producto:
                tiposProducto.append(tipo)
                productos.append(producto)
        # Obtenemos las fotos del formulario
        fotos = []
        for i in range(1,4):
            foto = request.files.get(f'foto{i}')
            if foto:
                fotos.append(foto)
        # Obtenemos los datos restantes del formulario
        descripcion = request.form.get('descripcion')
        region = request.form.get('region')
        comuna = request.form.get('comuna')
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        celular = request.form.get('celular')
        error = ""
        # Validamos los datos
        if not validate_add_product(tiposProducto, producto, descripcion, fotos, region, comuna, nombre, email, celular):
            error += "Uno de los datos entregados no es válido."
            #Si los datos no son válidos, redirigimos a la página de agregar producto con el mensaje de error
            return redirect(url_for("agregar_producto"))

        # Guardar fotos en carpeta uploads de static
        for foto in fotos:
            # Creamos un nombre único para la foto a guardar
            _filename = hashlib.sha256(
            secure_filename(foto.filename).encode("utf-8")).hexdigest()
            _extension = filetype.guess(foto).extension
            # Definimos el nombre de la foto
            img_filename = f"{_filename}.{_extension}"
            # Guardamos la foto en la carpeta "productos"
            foto.save(os.path.join(app.config["UPLOAD_FOLDER"], PRODUCT_FOLDER, img_filename))


        # Agregar producto a la base de datos aquí

        # Redirigimos a la página principal después de agregar el producto.
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