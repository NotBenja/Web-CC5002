//Llamamos a los elementos que requieren validación:
let tipo = document.getElementById('tipoPedido');
let region = document.getElementById("region");
let comuna = document.getElementById("comuna");
const nombre = document.getElementById("nombreComprador");
const email = document.getElementById("emailComprador");
const numero = document.getElementById("celularComprador");
const agregarPedidoBtn = document.getElementById("agregarPedido");
const confirmationMessage = document.getElementById("confirmationMessage");
const confirmarBtn = document.getElementById("confirmar");
const cancelarBtn = document.getElementById("cancelar");
const descripcion = document.getElementById("descripcion");

//Validaciones

const validarDescripcion = (descripcion) => {
  if (descripcion.value.trim() === "") {
    return true;
  }
  const largo = descripcion.value.trim().length;
  return largo <= 300;
};

const validarPedidos = (pedidos) => {
  let count = 0;
  pedidos.forEach(function(select) {
    if(select.value != "none"){
      count++;
    }  
  });
  return count > 0;
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
  let pedidos = document.querySelectorAll(".pedidos");
  if (!validarPedidos(pedidos)) {
    isValid = false;
    errorMessage += "Por favor, ingresa al menos una fruta/verdura.\n";
    pedidos.forEach(function(select) {
      select.style.borderColor = "red";
    });
  } else {
    pedidos.forEach(function(select) {
      select.style.borderColor = "";
    });
  }
  if (!validarDescripcion(descripcion)) {
    isValid = false;
    errorMessage += "Por favor, ingresa una descripción de hasta 300 caracteres.\n";
    descripcion.style.borderColor = "red";
  } else {
    descripcion.style.borderColor = "";
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

document.getElementById('agregarPedido').addEventListener('click', () => {
  handleFormSubmit();
});

document.getElementById('confirmar').addEventListener('click', () => {
  document.getElementById('orderForm').submit();
});

document.getElementById('cancelar').addEventListener('click', () => {
  document.getElementById('confirmationMessage').style.display = 'none';
});
