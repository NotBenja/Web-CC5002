//Creamos las listas necesarias
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

const regiones_comunas = {
  "regiones": [
      {
          "region": "Arica y Parinacota",
          "comunas": ["Arica", "Camarones", "Putre", "General Lagos"]
      },
      {
          "region": "Tarapacá",
          "comunas": ["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]
      },
      {
          "region": "Antofagasta",
          "comunas": ["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"]
      },
      {
          "region": "Atacama",
          "comunas": ["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"]
      },
      {
          "region": "Coquimbo",
          "comunas": ["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]
      },
      {
          "region": "Valparaíso",
          "comunas": ["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"]
      },
      {
          "region": "Región del Libertador Gral. Bernardo O’Higgins",
          "comunas": ["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]
      },
      {
          "region": "Región del Maule",
          "comunas": ["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"]
      },
      {
          "region": "Región de Ñuble",
          "comunas": ["Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ránquil", "Treguaco", "Bulnes", "Chillán Viejo", "Chillán", "El Carmen", "Pemuco", "Pinto", "Quillón", "San Ignacio", "Yungay", "Coihueco", "Ñiquén", "San Carlos", "San Fabián", "San Nicolás"]
      },
      {
          "region": "Región del Biobío",
          "comunas": ["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío"]
      },
      {
          "region": "Región de la Araucanía",
          "comunas": ["Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria"]
      },
      {
          "region": "Región de Los Ríos",
          "comunas": ["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"]
      },
      {
          "region": "Región de Los Lagos",
          "comunas": ["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"]
      },
      {
          "region": "Región Aisén del Gral. Carlos Ibáñez del Campo",
          "comunas": ["Coihaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O’Higgins", "Tortel", "Chile Chico", "Río Ibáñez"]
      },
      {
          "region": "Región de Magallanes y de la Antártica Chilena",
          "comunas": ["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "Antártica", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
      },
      {
          "region": "Región Metropolitana de Santiago",
          "comunas": ["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "Santiago", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]
       }
  ]
};
//Llamamos a los elementos que requieren validación:
const tipoProductos = document.querySelectorAll('.tipoProducto');
const producto = document.getElementById("producto");
const region = document.getElementById("region");
const comuna = document.getElementById("comuna");
const nombre = document.getElementById("nombreComprador");
const email = document.getElementById("emailComprador");
const numero = document.getElementById("celularComprador");
const agregarPedidoBtn = document.getElementById("agregarPedido");
const confirmationMessage = document.getElementById("confirmationMessage");
const confirmarBtn = document.getElementById("confirmar");
const cancelarBtn = document.getElementById("cancelar");



//Agregamos las regiones:
regiones_comunas.regiones.forEach((n_region) => {
  let nuevaRegion = document.createElement("option");
  nuevaRegion.value = n_region.region;
  nuevaRegion.text = n_region.region;
  region.appendChild(nuevaRegion);
});

// EventListener para cambiar la lista de comunas según la región seleccionada
region.addEventListener("change", () => {
  while (comuna.firstChild) {
    comuna.removeChild(comuna.firstChild);
  }
  const selectedRegion = region.value;
  const selectedRegionData = regiones_comunas.regiones.find((n_region) => n_region.region === selectedRegion);
  if (selectedRegionData) {
    selectedRegionData.comunas.forEach((n_comuna) => {
      let nuevaComuna = document.createElement("option");
      nuevaComuna.value = n_comuna;
      nuevaComuna.text = n_comuna;
      comuna.appendChild(nuevaComuna);
    });
  }
});





//Creador de listas para frutas/verduras
const crearLista = (tipoProducto) => {
  let lista = document.createElement("select");
  if (tipoProducto == "fruta") {
      for (let i = 0; i < frutas.length; i++) {
          const nuevoElemento = document.createElement("option");
          nuevoElemento.value = frutas[i];
          nuevoElemento.text = frutas[i];
          lista.appendChild(nuevoElemento);
      }
  } else if (tipoProducto == "verdura") {
      for (let i = 0; i < verduras.length; i++) {
          const nuevoElemento = document.createElement("option");
          nuevoElemento.value = verduras[i];
          nuevoElemento.text = verduras[i];
          lista.appendChild(nuevoElemento);
      }
  }
  return lista
}


//EventListener para que cada vez que se seleccione un tipo de producto aparezca/desaparezca la lista respectiva.
tipoProductos.forEach((producto, index) => {
  producto.addEventListener("change", () => {
      const contenedorId = 'contenedor' + (index + 1);
      const contenedor = document.getElementById(contenedorId);
      while (contenedor.firstChild) {
        contenedor.removeChild(contenedor.firstChild);
      }
      if(producto.value == "none"){
        return
      }
      let lista = crearLista(producto.value);
      contenedor.appendChild(lista);
  })
})

//Validaciones
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

const validarRegion_Comuna = (region, comuna) => {
  const selectedRegionData = regiones_comunas.regiones.find((n_region) => n_region.region === region);
  if (selectedRegionData) {
    if (selectedRegionData.comunas.includes(comuna)) {
      return true; 
    } 
    else {
      return false;
    }
  } 
  else {
    return false;
  }
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
  const num = numero.value.trim();
  const validez = /^\+569\d{8}$/.test(num);
  return validez;
};


const handleFormSubmit = () => {
  let isValid = true;
  let errorMessage = "";
  if (!validarTipo(tipoProductos)) {
    isValid = false;
    errorMessage += "Por favor, ingresa al menos un producto.\n";
    tipoProductos.forEach(function(select) {
      select.style.borderColor = "red";
    });
  } else {
    tipoProductos.forEach(function(select) {
      select.style.borderColor = "";
    });
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
  alert('Hemos recibido el registro de su pedido. ¡Muchas gracias!');
  window.location.href = "../index.html";
});

document.getElementById('cancelar').addEventListener('click', () => {
  document.getElementById('confirmationMessage').style.display = 'none';
});
