//Llamamos a los elementos que requieren validación:
let tipos = document.querySelectorAll('.tipoProducto');
let producto = document.getElementById("producto");
let region = document.getElementById("region");
let comuna = document.getElementById("comuna");
const fotos = document.querySelectorAll('input[type="file"]');
const nombre = document.getElementById("nombreProductor");
const email = document.getElementById("emailProductor");
const numero = document.getElementById("celularProductor");
const agregarProductoBtn = document.getElementById("agregarProducto");
const confirmationMessage = document.getElementById("confirmationMessage");
const confirmarBtn = document.getElementById("confirmar");
const cancelarBtn = document.getElementById("cancelar");

//Validaciones
const validarTipo = (tipoProductos) => {
  let productos = 0;
  
  tipoProductos.forEach(function(select) {
    if(select.value != "none"){
      productos++;
    }  
  });
  return productos > 0;
};

const validarFotos = (fotos) => {
  let conteoFotos = 0;
  const tiposValidos = ["image/jpeg", "image/png", "image/gif","image/jpg"];
  fotos.forEach(function(input) {
    if (input.files.length > 0) {
      const archivo = input.files[0];
      if (tiposValidos.includes(archivo.type)) {
        conteoFotos++;
      } else {return false}
    }
  });
  return conteoFotos > 0;
};


const validarRegion_Comuna = (region, comuna) => {
  if(region == "none" || comuna == "none"){
    return false
  }
  return true;
};

const validarNombre = (nombre) => {
  const largo = (nombre.value.trim()).length
  return largo >= 3 && largo <= 80;
};

const validarEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

const validarNumero = (numero) => {
  //En caso de haber un número, debe cumplir con la sintaxis correcta
  if(numero != null && numero.value.trim() != ""){
    const num = numero.value.trim();
    const validez = /^\+569\d{8}$/.test(num);
    return validez;
  } else {
    return true
  }
};


const handleFormSubmit = () => {
  let isValid = true;
  let errorMessage = "";
  if (!validarTipo(tipos)) {
    isValid = false;
    errorMessage += "Por favor, ingresa al menos un producto.\n";
    tipos.forEach(function(select) {
      select.style.borderColor = "red";
    });
  } else {
    tipos.forEach(function(select) {
      select.style.borderColor = "";
    });
  }

  if (!validarFotos(fotos)) {
    isValid = false;
    errorMessage += "Por favor, revisa si tus archivos son imágenes. Debe ser al menos una.\n";
  }

  if (!validarRegion_Comuna(region.value, comuna.value)) {
    isValid = false;
    errorMessage += "Por favor, selecciona una región/comuna válida.\n";
    region.style.borderColor = "red";
    comuna.style.borderColor = "red";
  } else {
    region.style.borderColor = "";
    comuna.style.borderColor = "";
  }

  if (!validarNombre(nombre)) {
    isValid = false;
    errorMessage += "Por favor, ingresa un nombre de entre 3 y 80 caracteres.\n";
    nombre.style.borderColor = "red";
  } else {
    nombre.style.borderColor = "";
  }

  if (!validarEmail(email.value)) {
    isValid = false;
    errorMessage += "Por favor, ingresa un correo electrónico válido.\n";
    email.style.borderColor = "red";
  } else {
    email.style.borderColor = "";
  }

  if (!validarNumero(numero)) {
    isValid = false;
    errorMessage += "Por favor, ingresa un número telefónico válido.\n";
    numero.style.borderColor = "red";
  } else {
    numero.style.borderColor = "";
  }

  if (!isValid) {
    alert(errorMessage);
    document.getElementById('confirmationMessage').style.display = 'none';
  } else {
    document.getElementById('confirmationMessage').style.display = 'block';
  }
};

document.getElementById('agregarProducto').addEventListener('click', () => {
  handleFormSubmit();
});

document.getElementById('confirmar').addEventListener('click', () => {
  document.getElementById('productForm').submit();
});

document.getElementById('cancelar').addEventListener('click', () => {
  document.getElementById('confirmationMessage').style.display = 'none';
});
