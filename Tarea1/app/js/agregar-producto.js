//Llamamos a los elementos que requieren validación:
const tipoProductos = document.querySelectorAll('.tipoProducto');
const producto = document.getElementById("producto");
const region = document.getElementById("region");
const comuna = document.getElementById("comuna");
const fotos = document.querySelectorAll('input[type="file"]');
const nombre = document.getElementById("nombreProductor");
const email = document.getElementById("emailProductor");
const numero = document.getElementById("celularProductor");


const agregarProductoBtn = document.getElementById("agregarProducto");
const confirmationMessage = document.getElementById("confirmationMessage");
const confirmarBtn = document.getElementById("confirmar");
const cancelarBtn = document.getElementById("cancelar");


const frutas = [
    "Arándano", "Frambuesa", "Frutilla", "Grosella", "Mora", "Limón", "Mandarina",
    "Naranja", "Pomelo", "Melón", "Sandía", "Palta", "Chirimoya", "Coco", "Dátil",
    "Kiwi", "Mango", "Papaya", "Piña", "Plátano", "Damasco", "Cereza", "Ciruela",
    "Higo", "Kaki", "Manzana", "Durazno", "Nectarin", "Níspero", "Pera", "Uva",
    "Almendra", "Avellana", "Maní", "Castaña", "Nuez", "Pistacho"
];
const verduras = [
    "Brócoli", "Repollo", "Coliflor", "Rábano", "Alcachofa", "Lechuga", "Zapallo",
    "Pepino", "Haba", "Maíz", "Champiñón", "Apio", "Perejil",
    "Ajo", "Cebolla", "Espárrago", "Puerro", "Acelga", "Espinaca", "Remolacha",
    "Berenjena", "Papa", "Pimiento", "Tomate", "Zanahoria"
];

const validarTipo = (tipoProductos) => {
  let conteoTiposValidos = 0;
  const tiposValidos = ["fruta", "verdura"];
  
  tipoProductos.forEach(function(select) {
    const tipoSeleccionado = select.value;
    if(tiposValidos.includes(tipoSeleccionado)){
      conteoTiposValidos++;
    }  
  });
  
  return conteoTiposValidos > 0;
};

const validarFotos = (fotos) => {
  let conteoFotos = 0;

  fotos.forEach(function(input) {
    if (input.files.length > 0) {
      conteoFotos++;
    }
  });
  return conteoFotos > 0;
};

const validarNombre = (nombre) => {
  const largo = (nombre.value.trim()).length
  return (largo>=3) && (largo <= 80);
};

const validarEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

const validarNumero = (numero) => {
  const num = numero.value.trim()
  const validez = /^\+569\d{8}$/.test(num);
  return validez;
}