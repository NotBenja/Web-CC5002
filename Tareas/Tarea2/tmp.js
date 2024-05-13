   //Listas de frutas y verduras
   const lista_frutas = {{frutas|tojson|safe}};
   const lista_verduras = {{verduras|tojson|safe}};

   //Creador de listas para frutas/verduras
   const crearLista = (tipoProducto, i) => {
   let lista = document.createElement("select");
   lista.name = "producto" + (i + 1);
   if (tipoProducto == "fruta") {
       for (let i = 0; i < lista_frutas.length; i++) {
           let fruta;
           if (typeof lista_frutas[i] === 'string') {
               const partes = lista_frutas[i].split(",");
               fruta = partes[1];
           } else {
               fruta = lista_frutas[i][1];
           }
           const nuevoElemento = document.createElement("option");
           nuevoElemento.value = fruta;
           nuevoElemento.text = fruta;
           lista.appendChild(nuevoElemento);
       }
   } else if (tipoProducto == "verdura") {
       for (let i = 0; i < lista_verduras.length; i++) {
           let verdura;
           if (typeof lista_verduras[i] === 'string') {
               const partes = lista_verduras[i].split(",");
               verdura = partes[1];
           } else {
               verdura = lista_verduras[i][1];
           }
           const nuevoElemento = document.createElement("option");
           nuevoElemento.value = verdura;
           nuevoElemento.text = verdura;
           lista.appendChild(nuevoElemento);
       }
   }
   return lista;
   };

   //EventListener para que cada vez que se seleccione un tipo de producto aparezca/desaparezca la lista respectiva.
   const tipoProductos = document.querySelectorAll(".tipoProducto");
   tipoProductos.forEach((producto, index) => {
       producto.addEventListener("change", () => {
           const contenedorId = 'contenedor' + (index + 1);
           const contenedor = document.getElementById(contenedorId);
           while (contenedor.firstChild) {
               contenedor.removeChild(contenedor.firstChild);
           }
           if (producto.value == "none") {
               return;
           }
           let lista = crearLista(producto.value, index);
           contenedor.appendChild(lista);
       });
   });
   
   //Agregamos las regiones y comunas
   const dicc_comunas = {{ comunas|tojson|safe }};
   const region = document.getElementById("region");
   const comuna = document.getElementById("comuna");

   //EventListener para cambiar la lista de comunas según la región seleccionada
   region.addEventListener("change", () => {
       while (comuna.firstChild) {
           comuna.removeChild(comuna.firstChild);
       }
       const selectedRegionId = region.value;
       if(selectedRegionId == "none") {
           let opcion = document.createElement("option");
           opcion.value = "none";
           opcion.text = "Seleccionar";
           comuna.appendChild(opcion);
           return;
       }
       const selectedRegionComunas = dicc_comunas[selectedRegionId];
       if (selectedRegionComunas) {
           selectedRegionComunas.forEach((n_comuna) => {
               let nuevaComuna = document.createElement("option");
               nuevaComuna.value = n_comuna[0];
               nuevaComuna.text = n_comuna[1];
               comuna.appendChild(nuevaComuna);
           });
       }
   });
