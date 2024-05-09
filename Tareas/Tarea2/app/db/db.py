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
def get_productos_recientes():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_productos_recientes"])
	products = cursor.fetchall()
	return products

def get_productos_recientes_limitado():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_productos_recientes_limitado"])
	products = cursor.fetchall()
	return products

def get_productos_siguientes():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_productos_siguientes"])
	products = cursor.fetchall()
	return products

def get_productos_comuna():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_productos_comuna"])
	products = cursor.fetchall()
	return products

def get_tipos_producto(producto_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_tipos_producto"], (producto_id,))
	tipos = cursor.fetchall()
	return tipos

def get_fotos_producto(producto_id):
	"""
    Retorna la ruta del archivo de la foto y el nombre del archivo con el id entregado.
    """
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_fotos_producto"], (producto_id,))
	fotos = cursor.fetchall()
	return fotos

def get_ultimo_id_insertado():
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["obtener_ultimo_id_insertado"])
	last_id = cursor.fetchone()
	return last_id[0]

# Definimos funciones para insertar productos en la db
def insertar_producto(tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_producto"], (tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor))
	conn.commit()

def insertar_producto_verdura_tipo(producto_id, tipo_verdura_fruta_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_producto_verdura_tipo"], (producto_id, tipo_verdura_fruta_id))
	conn.commit()

def insertar_foto(ruta_archivo, nombre_archivo, producto_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["insertar_foto"], (ruta_archivo, nombre_archivo, producto_id))
	conn.commit()


	
#Definimos funciones para registrar productos en la db
def registrar_producto(tipoProducto, producto, descripcion, fotos, region, comuna, nombre, email, celular):
	#Verificamos si el producto ya existe
	existing_products = get_productos_recientes()
	for product in existing_products:
		if product[0] == tipoProducto and product[1] == descripcion and product[2] == comuna:
			return False, "El producto ya existe."
	
	#En caso de no existir, lo agregamos
	insertar_producto(tipoProducto, descripcion, comuna, nombre, email, celular)
	
	#Obtenemos el id del producto para insertarlo en las demás tablas
	producto_id = get_ultimo_id_insertado()
	insertar_producto_verdura_tipo(producto_id, tipoProducto)
	
	return True, None

#def insertar_foto(ruta_archivo, nombre_archivo, producto_id):
# Esta función quiero que construyas
