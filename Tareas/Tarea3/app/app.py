from flask import Flask, request, render_template, redirect, url_for, session, jsonify, flash
from utils.validations import validate_add_product
from utils.validations import validate_add_order
from db import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
from datetime import datetime
from PIL import Image
from flask_cors import cross_origin



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
    if request.method == 'GET':
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
    # Si el método es POST, se envia el formulario
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
    # Si el método es GET, mostramos el formulario para agregar un producto
    elif request.method == 'GET':
        return render_template('productos/agregar-producto.html', frutas = frutas, verduras = verduras, regiones=regiones, comunas=comunas)
    
# Función para paginar los productos con un tamaño de página y un número de página
def paginate_productos(page: int, per_page: int) -> list:
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    return db.get_productos_recientes()[start_index:end_index]

@app.route('/ver-productos', methods=['GET'])
def ver_productos():
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        PAGE_SIZE = 5
        productos_paginados = paginate_productos(page, PAGE_SIZE)
        data = []
        for producto in productos_paginados:
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
            foto_nombre = fotos[0][1]
            foto_producto = f"/uploads/productos/small/{fotos[0][1]}" 
            # Juntamos todos los datos para dejarlos como contexto para la plantilla
            data.append({
                "id": producto_id,
                "tipo": tipo,
                "nombre": nombre_productor,
                "comuna": region_comuna[0][0],
                "region": region_comuna[0][1],
                "foto_nombre": foto_nombre, 
                "foto": foto_producto,
                "productos": detalle_productos[:-2], # Quitamos la coma y el espacio en blanco
            })

        next_url = url_for('ver_productos', page=page + 1) if len(db.get_productos_recientes()) > page * PAGE_SIZE else None
        prev_url = url_for('ver_productos', page=page - 1) if page > 1 else None
        return render_template("productos/ver-productos.html", filas=data, next_url=next_url, prev_url=prev_url, page=page)



@app.route('/agregar-pedido', methods=['GET', 'POST'])
def agregar_pedido():
    frutas = db.get_frutas()
    verduras = db.get_verduras()
    regiones = db.get_regiones()
    comunas = {}
    for region in regiones:
        region_id = region[0]
        comunas[region_id] = db.get_comunas_por_regionid(region_id)
    # Si el método es POST, se envia el formulario
    if request.method == 'POST':
        # Definimos una variable para los mensajes de errores
        error = ""
        # Obtenemos los productos con su tipo
        tipoPedido = request.form.get(f'tipoPedido')
        pedidos = []
        for i in range(1,6):
            pedido = request.form.get(f'Pedido{i}')
            if pedido != "none" and pedido.strip() != "" and pedido not in pedidos:
                pedidos.append(pedido)

        # Obtenemos los datos restantes del formulario
        descripcion = request.form.get('Descripcion')
        region = request.form.get('region')
        comuna = request.form.get('comuna')
        nombre = request.form.get('nombreComprador')
        email = request.form.get('emailComprador')
        celular = request.form.get('celularComprador')

        # Validamos los datos
        if not validate_add_order(tipoPedido, pedidos, descripcion, region, comuna, nombre, email, celular):
            error += "Uno de los datos entregados no es válido."
            # Si los datos no son válidos, redirigimos a la página de agregar producto con el mensaje de error
            return render_template('productos/agregar-producto.html', error=error, frutas = frutas, verduras = verduras, regiones=regiones, comunas=comunas)
        # Agregar producto a la base de datos aquí
        db.registrar_pedido(tipoPedido, pedidos, descripcion, comuna, nombre, email, celular)
        # Redirigimos a la página principal después de agregar el producto.
        msg = "Pedido agregado exitosamente."
        flash(msg)
        return redirect(url_for('index'))
    # Si el método es GET, mostramos el formulario para agregar un producto
    elif request.method == 'GET':
        return render_template('pedidos/agregar-pedido.html', frutas = frutas, verduras = verduras, regiones=regiones, comunas=comunas)

# Función para paginar los pedidos con un tamaño de página y un número de página
def paginate_pedidos(page: int, per_page: int) -> list:
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    return db.get_pedidos_recientes()[start_index:end_index]


@app.route('/ver-pedidos', methods=['GET'])
def ver_pedidos():
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        PAGE_SIZE = 5
        pedidos_paginados = paginate_pedidos(page, PAGE_SIZE)
        data = []
        for pedido in pedidos_paginados:
            # Obtenemos los datos del pedido
            pedido_id, tipo, descripcion, comuna_id, nombre_comprador, email_comprador, celular_comprador = pedido
            # Cambiamos los textos a un formato mejor
            if tipo == "fruta":
                tipo = "Fruta"
            elif tipo == "verdura":
                tipo = "Verdura"
            # Vemos los productos que anotó el comprador
            pedidos_query = db.get_tipos_pedido(pedido_id)
            pedidos_query = [pedido[0] for pedido in pedidos_query]
            
            detalle_pedidos = ""
            for pedido in pedidos_query:
                detalle_pedidos += pedido + ", "

            # Obtenemos el nombre de la región y la comuna
            region_comuna = db.get_nombre_comuna_y_region_por_id_comuna(comuna_id)
            # Juntamos todos los datos para dejarlos como contexto para la plantilla
            data.append({
                "id": pedido_id,
                "tipo": tipo,
                "nombre": nombre_comprador,
                "comuna": region_comuna[0][0],
                "region": region_comuna[0][1],
                "productos": detalle_pedidos[:-2], # Quitamos la coma y el espacio en blanco
            })

        next_url = url_for('ver_pedidos', page=page + 1) if len(db.get_pedidos_recientes()) > page * PAGE_SIZE else None
        prev_url = url_for('ver_pedidos', page=page - 1) if page > 1 else None
        return render_template("pedidos/ver-pedidos.html", filas=data, next_url=next_url, prev_url=prev_url, page=page)




@app.route('/ver-pedidos/informacion-pedido', methods=['GET'])
def informacion_pedido():
    if request.method == 'GET':
        # Llamamos a los argumentos entregados en la url
        id_pedido = request.args.get('id')
        tipo= request.args.get('tipo')
        pedidos = request.args.get('pedidos')
        region = request.args.get('region')
        comuna = request.args.get('comuna')
        datos_restantes = db.get_datos_pedido_por_id(id_pedido)
        nombre = datos_restantes[0]
        email = datos_restantes[1]
        celular = datos_restantes[2]
        # Si hay algun dato faltante, se reemplaza por uno predeterminado
        if celular == None or celular == "":
            celular = "No hay celular disponible."
        descripcion = datos_restantes[3]
        if descripcion == None or descripcion == "":
            descripcion = "No hay descripción disponible."
        # Hacemos un diccionario con los datos para el contexto
        data = {
            "id": id_pedido,
            "tipo": tipo,
            "pedidos": pedidos,
            "region": region,
            "comuna": comuna,
            "nombre": nombre,
            "email": email,
            "celular": celular,
            "descripcion": descripcion
        }
        return render_template('pedidos/informacion-pedido.html', data=data)
    


@app.route('/ver-productos/informacion-producto', methods=['GET'])
def informacion_producto():
    if request.method == 'GET':
        # Llamamos a los argumentos entregados en la url
        id_producto = request.args.get('id')
        tipo= request.args.get('tipo')
        productos = request.args.get('productos')
        region = request.args.get('region')
        comuna = request.args.get('comuna')
        fotos_ = db.get_fotos_producto(id_producto)
        fotos = []
        for foto_ in fotos_:
            if foto_[0] == "productos/medium":
                foto_ = f"/uploads/{foto_[0]}/{foto_[1]}"
                print(foto_)
                fotos.append(foto_)
        datos_restantes = db.get_datos_producto_por_id(id_producto)
        nombre = datos_restantes[0]
        email = datos_restantes[1]
        celular = datos_restantes[2]
        # Si hay algun dato faltante, se reemplaza por uno predeterminado
        if celular == None or celular == "":
            celular = "No hay celular disponible."
        descripcion = datos_restantes[3]
        if descripcion == None or descripcion == "":
            descripcion = "No hay descripción disponible."
        # Hacemos un diccionario con los datos para el contexto
        data = {
            "id": id_producto,
            "tipo": tipo,
            "productos": productos,
            "region": region,
            "comuna": comuna,
            "fotos": fotos,
            "nombre": nombre,
            "email": email,
            "celular": celular,
            "descripcion": descripcion
        }
        return render_template('productos/informacion-producto.html', data=data)


@app.route('/stats', methods=['GET'])
def stats():
    if request.method == 'GET':
        return render_template('stats.html')

@app.route("/stats/grafico-productos", methods=["GET"])
def grafico_productos():
    return render_template("productos/grafico-productos.html")

@app.route("/stats/grafico-pedidos", methods=["GET"])
def grafico_pedidos():
    return render_template("pedidos/grafico-pedidos.html")


@app.route("/get-datos-productos", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_datos_productos():
    data = db.get_cantidad_productos()
    return jsonify(data)


@app.route("/get-datos-pedidos", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_datos_pedidos():
    data = db.get_cantidad_pedidos_comuna()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)