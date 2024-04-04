const tipoProducto = document.getElementById("tipoProducto");
const producto = document.getElementById("producto");
const region = document.getElementById("region");
const comuna = document.getElementById("comuna");
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

// Función para llenar el menú de selección de productos según el tipo seleccionado
tipoProducto.addEventListener("change", function() {
    // Limpiar el menú de selección de productos antes de agregar nuevas opciones
    while (producto.firstChild) {
        producto.removeChild(producto.firstChild);
    }
    if (tipoProducto.value === "fruta") {
        generarCheckboxes(frutas)
    } else if (tipoProducto.value === "verdura") {
       generarCheckboxes(verduras)
    }
});

const generarCheckboxes = (tipo) =>{
    // Limpiar productosDiv
    const productosDiv = document.getElementById("productos");

    // Iterar sobre la lista de productos y crear un checkbox para cada uno
    tipo.forEach(function(producto) {
      // Crear el checkbox
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.name = "producto";
      checkbox.value = producto;

      // Agregar un event listener para controlar la cantidad de elementos seleccionados
      checkbox.addEventListener("change", function() {
        const checkboxesSeleccionados = productosDiv.querySelectorAll("input[type='checkbox']:checked");
        if (checkboxesSeleccionados.length > 5) {
          this.checked = false; // Desmarcar el checkbox si se excede el límite de selección
        }
      });

      // Crear la etiqueta para el checkbox
      const label = document.createElement("label");
      label.textContent = producto;

      // Agregar el checkbox y la etiqueta al contenedor
      productosDiv.appendChild(checkbox);
      productosDiv.appendChild(label);
      productosDiv.appendChild(document.createElement("br")); // Salto de línea
    });
  };

  // Llamar a la función para generar los checkboxes


// Función para llenar el menú de selección de comunas según la región seleccionada
region.addEventListener("change", function() {
    // Lógica para llenar el menú de selección de comunas según la región seleccionada
});

const validateEmail = email => {
    // Email validation using a regular expression
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };
  
  const handleFormSubmit = () => {
    console.log("Validating form...");
  
    const emailInput = document.getElementById("email");
    const userNameInput = document.getElementById("username");
    const passwordInput = document.getElementById("contrasenna");
  
    let isValid = true;
    let errorMessage = "";
  
    // Validate inputs
    if (!validateEmail(emailInput.value)) {
      isValid = false;
      errorMessage += "Por favor, ingresa un correo electrónico válido.\n";
      emailInput.style.borderColor = "red";
    } else {
      emailInput.style.borderColor = "";
    }
  
    if (!validateUserName(userNameInput.value)) {
      isValid = false;
      errorMessage += "Por favor, ingresa un nombre de usuario válido (5 caracteres mínimo).\n";
      userNameInput.style.borderColor = "red";
    } else {
      userNameInput.style.borderColor = "";
    }
  
    if (!validatePassword(passwordInput.value)) {
      isValid = false;
      errorMessage += "La contraseña debe tener al menos 8 caracteres, incluyendo un número, una minúscula y una mayúscula.\n";
      passwordInput.style.borderColor = "red";
    } else {
      passwordInput.style.borderColor = "";
    }
  
    // Handle errors or redirect to confessions page
    if (!isValid) {
      alert(errorMessage); // Replace with a user-friendly error display
    } else {
      // Store username in localStorage
      const username = userNameInput.value;
      localStorage.setItem("username", username);
  
      // Redirect to confessions page
      window.location.href = "../html/confesiones.html";
    }
  };
  
  // --- Event Listener ---
  
  const submitButton = document.getElementById("confirmationMessage");
  submitButton.addEventListener("click", handleFormSubmit);
// Evento click para el botón "Agregar Producto(s)"
agregarProductoBtn.addEventListener("click", function() {
    if (validarFormulario()) {
        // Si la validación pasa, mostrar mensaje de confirmación
        confirmationMessage.style.display = "block";
    } else {
        // Si la validación falla, mostrar mensaje de error
        alert("Por favor complete todos los campos obligatorios (*) correctamente.");
    }
});

// Evento click para el botón "Sí, confirmo"
confirmarBtn.addEventListener("click", function() {
    // Mostrar mensaje de confirmación final
    alert("Hemos recibido el registro de producto. Muchas gracias.");
    // Redireccionar a la portada (index.html)
    window.location.href = "index.html";
});

// Evento click para el botón "No, quiero volver al formulario"
cancelarBtn.addEventListener("click", function() {
    // Ocultar mensaje de confirmación y volver al formulario
    confirmationMessage.style.display = "none";
});
