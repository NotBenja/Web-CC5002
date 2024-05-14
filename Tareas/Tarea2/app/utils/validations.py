import filetype
import re

def validate_email(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(email_regex, email):
        return True
    else:
        return False

def validate_foto(foto):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if foto is None:
        return False

    # check if the browser submitted an empty file
    if foto.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(foto)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validate_numero(numero):
    # En caso de haber un número, debe cumplir con la sintaxis correcta
    if numero is not None and numero.strip() != "":
        num = numero.strip()
        validez = bool(re.match(r'^\+569\d{8}$', num))
        return validez
    else:
        return True
def validate_nombre(nombre):
    lenght = len(nombre)
    return (3 <= lenght <= 80)

def validate_products(productos):
    count = 0
    for producto in productos:
        if producto != "none":
            count += 1
    return count > 0

def validate_product_description(descripcion):
    return True

def validate_product_photos(fotos):
    for foto in fotos:
        if not validate_foto(foto):
            return False
    return True

def validate_product_location(region, comuna):
    return True

def validate_product_producer(nombre, email, celular):
    if not validate_nombre(nombre):
        return False
    if not validate_email(email):
        return False 
    if not validate_numero(celular):
        return False
    return True

# Aquí se valida todo el formulario
def validate_add_product(tipoProducto, productos, descripcion, fotos, region, comuna, nombre, email, celular):
    if tipoProducto == "none":
        return False
    if not validate_products(productos):
        return False
    if not validate_product_description(descripcion):
        return False
    if not validate_product_photos(fotos):
        return False
    if not validate_product_location(region, comuna):
        return False
    if not validate_product_producer(nombre, email, celular):
        return False
    return True
