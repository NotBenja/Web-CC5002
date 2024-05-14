from flask import Flask, request, render_template, redirect, url_for, flash
from utils.validations import validate_add_product
from db import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
from datetime import datetime
from PIL import Image


UPLOAD_FOLDER = 'static/uploads'
PRODUCT_FOLDER = 'productos'
sizes = {"/small":(120, 120), "/medium":(640, 480), "/big":(1280, 1024)}

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000 # 16 MB

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'El tamaño máximo por archivo es de 16MB.', 413

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/agregar-producto', methods=['GET', 'POST'])

def agregar_producto():
    frutas = db.get_frutas()
    verduras = db.get_verduras()
    regiones = db.get_regiones()
    comunas = {}
    for region in regiones:
        region_id = region[0]
        comunas[region_id] = db.get_comunas_por_regionid(region_id)
    if request.method == 'POST':
        # Definimos una variable para los mensajes de errores
        error = ""
        # Obtenemos los productos con su tipo
        tipoProducto = request.form.get(f'tipoProducto')
        productos = []
        for i in range(1,6):
            producto = request.form.get(f'Producto{i}')
            if producto != "none" and producto.strip() != "" and producto not in productos:
                productos.append(producto)
        # Obtenemos las fotos del formulario
        fotos = []
        for i in range(1,4):
            foto = request.files.get(f'foto{i}')
            if foto:
                fotos.append(foto)
        # Obtenemos los datos restantes del formulario
        descripcion = request.form.get('Descripcion')
        region = request.form.get('region')
        comuna = request.form.get('comuna')
        nombre = request.form.get('nombreProductor')
        email = request.form.get('emailProductor')
        celular = request.form.get('celularProductor')

        # Validamos los datos
        if not validate_add_product(tipoProducto, productos, descripcion, fotos, region, comuna, nombre, email, celular):
            error += "Uno de los datos entregados no es válido."
            # Si los datos no son válidos, redirigimos a la página de agregar producto con el mensaje de error
            return render_template('productos/agregar-producto.html', error=error, frutas = frutas, verduras = verduras, regiones=regiones, comunas=comunas)
        # Agregar producto a la base de datos aquí
        id_producto = db.registrar_producto(tipoProducto, productos, descripcion, comuna, nombre, email, celular)[2]
        # Guardar fotos en carpeta uploads de static
        i = 0
        for foto in fotos:
            # Creamos un nombre único para la foto a guardar
            _filename = hashlib.sha256(
            secure_filename(foto.filename).encode("utf-8")).hexdigest()
            _extension = filetype.guess(foto).extension

            #Calculamos la fecha exacta de subida del archivo
            now = datetime.now()
            # Usamos el formato año-mes-día hora:minuto:segundo
            uploadDate = now.strftime("%Y-%m-%d_%H-%M-%S")
            # Definimos el nombre de la foto
            img_filename = f"{_filename}_{uploadDate}_{i}.{_extension}"
            # Guardamos la foto original en la carpeta "productos"
            path = os.path.join(app.config["UPLOAD_FOLDER"], 
                                PRODUCT_FOLDER +"/original", 
                                img_filename)
            foto.save(path)
            # Creamos las otras resoluciones de la foto
            for folder, size in sizes.items():
                with Image.open(path) as img:
                    resized_img = img.resize(size)
                    new_path = os.path.join(app.config["UPLOAD_FOLDER"], 
                                            PRODUCT_FOLDER + folder , 
                                            img_filename)
                    resized_img.save(new_path)
                    db.insertar_foto(PRODUCT_FOLDER + folder, img_filename, id_producto)

            i += 1
            # Insertamos la foto en la base de datos
            db.insertar_foto(PRODUCT_FOLDER+"/original", img_filename, id_producto)


        # Redirigimos a la página principal después de agregar el producto.
        msg = "Producto agregado exitosamente."
        flash(msg)
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('productos/agregar-producto.html', frutas = frutas, verduras = verduras, regiones=regiones, comunas=comunas)
    

from flask import render_template, request, url_for

@app.route('/ver-productos', methods=['GET'])
def ver_productos():
    # Definimos la paginación para los productos, con un máximo de 5 productos por página
    PAGE_SIZE = 5
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * PAGE_SIZE

    data = []
    productos = db.get_productos_recientes_limitado()[offset: offset + PAGE_SIZE]
    for producto in productos:
        # Obtenemos los datos del producto
        producto_id, tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor = producto
        # Cambiamos los textos a un formato mejor
        if tipo == "fruta":
            tipo = "Fruta"
        elif tipo == "verdura":
            tipo = "Verdura"
        # Vemos los productos que anotó el productor
        productos_query = db.get_tipos_producto(producto_id)
        productos_query = [producto[0] for producto in productos_query]
        
        detalle_productos = ""
        for producto in productos_query:
            detalle_productos += producto + ", "

        # Obtenemos el nombre de la región y la comuna
        region_comuna = db.get_nombre_comuna_y_region_por_id_comuna(comuna_id)
        # Obtenemos las fotos del producto
        fotos = db.get_fotos_producto(producto_id)
        foto_producto = f"/uploads/productos/small/{fotos[0][1]}" 
        # Juntamos todos los datos para dejarlos como contexto para la plantilla
        data.append({
            "tipo": tipo,
            "nombre": nombre_productor,
            "comuna": region_comuna[0][0],
            "region": region_comuna[0][1],  
            "foto": foto_producto,
            "productos": detalle_productos[:-2] # Quitamos la coma y el espacio en blanco
        })

    next_url= url_for('ver_productos', page=page + 1) if len(db.get_productos_recientes_limitado()) > offset + PAGE_SIZE else None
    prev_url= url_for('ver_productos', page=page - 1) if page > 1 else None
    return render_template("productos/ver-productos.html", filas=data, next_url=next_url, prev_url=prev_url)

@app.route('/agregar-pedido', methods=['GET', 'POST'])
def agregar_pedido():
    if request.method == 'POST':
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