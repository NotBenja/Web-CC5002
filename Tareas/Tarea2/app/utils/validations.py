import filetype

def validate_email(value):
    return "@" in value


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

# Validaciones a definir

def validate_product_type(tiposProducto, productos):
    return True

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
    return True

# Aquí se valida todo el formulario
def validate_add_product(tipoProducto, producto, descripcion, fotos, region, comuna, nombre, email, celular):
    if not validate_product_type(tipoProducto, producto):
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
