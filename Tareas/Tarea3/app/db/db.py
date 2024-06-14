import pymysql
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

with open('db/querys.json', 'r') as querys:
	QUERY_DICT = json.load(querys)


def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn

# Traspasamos las querys del archivo sentencias.sql a funciones

# Definimos getters del listado de productos existentes en la db
def get_tipos_producto(producto_id):
	conn = get_conn()
	cursor = conn.cursor()
	query = "SELECT TVF.nombre FROM tipo_verdura_fruta TVF, producto_verdura_fruta PVF WHERE TVF.id=PVF.tipo_verdura_fruta_id AND PVF.producto_id=%s"
	cursor.execute(query, (producto_id,))
	result = cursor.fetchall()
	conn.close()
	return result

def get_tipos_pedido(pedido_id):
	conn = get_conn()
	cursor = conn.cursor()
	query = "SELECT TVF.nombre FROM tipo_verdura_fruta TVF, pedido_verdura_fruta PVF WHERE TVF.id=PVF.tipo_verdura_fruta_id AND PVF.pedido_id=%s"
	cursor.execute(query, (pedido_id,))
	result = cursor.fetchall()
	conn.close()
	return result

def get_productos_recientes():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_productos_recientes"])
	products = cursor.fetchall()
	conn.close()
	return products

def get_pedidos_recientes():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_pedidos_recientes"])
	pedidos = cursor.fetchall()
	conn.close()
	return pedidos


def get_productos_recientes_limitado():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_productos_recientes_limitado"])
	products = cursor.fetchall()
	conn.close()
	return products

def get_productos_siguientes():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_productos_siguientes"])
	products = cursor.fetchall()
	conn.close()
	return products

def get_productos_comuna():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_productos_comuna"])
	products = cursor.fetchall()
	conn.close()
	return products

def get_frutas():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_frutas"])
	frutas = cursor.fetchall()
	conn.close()
	return frutas

def get_verduras():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_verduras"])
	verduras = cursor.fetchall()
	conn.close()
	return verduras

def get_regiones():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_regiones"])
	regiones = cursor.fetchall()
	conn.close()
	return regiones

def get_comunas_por_regionid(region_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_comunas_por_region"], (region_id,))
	comunas = cursor.fetchall()
	conn.close()
	return comunas

def get_nombre_comuna_y_region_por_id_comuna(comuna_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_nombre_comuna_y_region_por_id_comuna"], (comuna_id,))
	nombres = cursor.fetchall()
	conn.close()
	return nombres

def get_fotos_producto(producto_id):
	"""
	Retorna la ruta del archivo de la foto y el nombre del archivo con el id entregado.
	"""
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_fotos_producto"], (producto_id,))
	fotos = cursor.fetchall()
	conn.close()
	return fotos

def get_ultimo_id_insertado():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_ultimo_id_insertado"])
	last_id = cursor.fetchone()
	conn.close()
	return last_id[0]

def get_datos_producto_por_id(producto_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_datos_producto_por_id"], (producto_id,))
	datos = cursor.fetchone()
	conn.close()
	return datos

def get_datos_pedido_por_id(pedido_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_datos_pedido_por_id"], (pedido_id,))
	datos = cursor.fetchone()
	conn.close()
	return datos


# Definimos funciones para insertar productos en la db
def insertar_producto(tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_producto"], (tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor))
	conn.commit()
	conn.close()

def insertar_producto_verdura_tipo(producto_id, tipo_verdura_fruta_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_producto_verdura_tipo"], (producto_id, tipo_verdura_fruta_id))
	conn.commit()
	conn.close()

def insertar_foto(ruta_archivo, nombre_archivo, producto_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_foto"], (ruta_archivo, nombre_archivo, producto_id))
	conn.commit()
	conn.close()



# Definimos funciones para registrar productos en la db
def registrar_producto(tipoProducto, productos, descripcion, comuna, nombre, email, celular):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_producto"], 
				   (tipoProducto, descripcion, comuna, nombre, email, celular))
	# Obtenemos el id del producto para insertarlo en las demás tablas
	cursor.execute(QUERY_DICT["obtener_ultimo_id_insertado"])
	last_id = cursor.fetchone()
	producto_id = last_id[0]
	for producto in productos:
		if producto.isdigit():
			producto = int(producto)
			cursor.execute(QUERY_DICT["insertar_producto_verdura_tipo"], (producto_id, producto))
	conn.commit()
	conn.close()
	return True, None, producto_id

def registrar_pedido(tipoPedido, pedidos, descripcion, comuna, nombre, email, celular):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_pedido"], 
				   (tipoPedido, descripcion, comuna, nombre, email, celular))
	# Obtenemos el id del producto para insertarlo en las demás tablas
	cursor.execute(QUERY_DICT["obtener_ultimo_id_insertado"])
	last_id = cursor.fetchone()
	pedido_id = last_id[0]
	for pedido in pedidos:
		if pedido.isdigit():
			pedido = int(pedido)
			cursor.execute(QUERY_DICT["insertar_pedido_verdura_tipo"], (pedido_id, pedido))
	conn.commit()
	conn.close()
	return True, None


# Funciones para los graficos

def get_cantidad_productos():
	frutas = 0
	verduras = 0
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_cantidad_productos_por_tipo"])
	producto_cantidad = cursor.fetchall()
	for producto in producto_cantidad:
		id_producto = int(producto[0])
		if id_producto < 38:
			frutas += producto[1]
		else:
			verduras += producto[1]
	conn.close()
	return frutas, verduras

def get_cantidad_pedidos_comuna():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_cantidad_pedidos_por_comuna"])
	pedido_cantidad = cursor.fetchall()
	conn.close()
	comuna_cantidad = {}
	for pedido in pedido_cantidad:
		comuna_cantidad[pedido[0]] = pedido[1]
	return comuna_cantidad