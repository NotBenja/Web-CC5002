import pymysql
import json

DB_NAME = "frutiverde_db"
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


	

# -- db-related functions --
def registrar_producto(tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor):
	# 1. Check if the product already exists
	existing_products = get_productos_recientes()
	for product in existing_products:
		if product[0] == tipo and product[1] == descripcion and product[2] == comuna_id:
			return False, "El producto ya existe."
	
	# 2. Insert the product into the database
	insertar_producto(tipo, descripcion, comuna_id, nombre_productor, email_productor, celular_productor)
	
	# 3. Get the last inserted product ID
	producto_id = get_ultimo_id_insertado()
	
	# 4. Insert the product type into the database
	insertar_producto_verdura_tipo(producto_id, tipo_verdura_fruta_id)
	
	# 5. Insert the product photo into the database
	insertar_foto(ruta_archivo, nombre_archivo, producto_id)
	
	return True, None





def get_user_by_email(email):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_user_by_email"], (email,))
	user = cursor.fetchone()
	return user

def get_user_by_username(username):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_user_by_username"], (username,))
	user = cursor.fetchone()
	return user

def create_user(username, password, email):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_user"], (username, password, email))
	conn.commit()

def get_confessions(page_size):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["get_confessions"], (page_size,))
	confessions = cursor.fetchall()
	return confessions

def create_confession(conf_text, conf_img, user_id):
	conn = get_conn()
	cursor = conn.cursor()
	cursor.execute(QUERY_DICT["create_confession"], (conf_text, conf_img, user_id))
	conn.commit()
def register_user(username, password, email):
	# 1. check the email is not in use
	_email_user = get_user_by_email(email)
	if _email_user is not None:
		return False, "El correo ya esta en uso."
	# 2. check the username is not in use
	_username_user = get_user_by_username(username)
	if _username_user is not None:
		return False, "El nombre de usuario esta en uso."
	# 3. create user
	create_user(username, password, email)
	return True, None

def login_user(username, password):
	a_user = get_user_by_username(username)
	if a_user is None:
		return False, "Usuario o contraseña incorrectos."

	a_user_passwd = a_user[3]
	if a_user_passwd != password:
		return False, "Usuario o contraseña incorrectos."
	return True, None

