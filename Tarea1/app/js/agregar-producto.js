document.addEventListener("DOMContentLoaded", function() {
    const tipoProducto = document.getElementById("tipoProducto");
    const producto = document.getElementById("producto");
    const region = document.getElementById("region");
    const comuna = document.getElementById("comuna");
    const agregarProductoBtn = document.getElementById("agregarProducto");
    const confirmationMessage = document.getElementById("confirmationMessage");
    const confirmarBtn = document.getElementById("confirmar");
    const cancelarBtn = document.getElementById("cancelar");

    // Función para llenar el menú de selección de productos según el tipo seleccionado
    tipoProducto.addEventListener("change", function() {
        if (tipoProducto.value === "fruta") {
            producto.innerHTML = `
                <option value="manzana">Manzana</option>
                <option value="banana">Banana</option>
                <option value="uva">Uva</option>
                <!-- Agregar más opciones según sea necesario -->
            `;
        } else if (tipoProducto.value === "verdura") {
            producto.innerHTML = `
                <option value="zanahoria">Zanahoria</option>
                <option value="lechuga">Lechuga</option>
                <option value="tomate">Tomate</option>
                <!-- Agregar más opciones según sea necesario -->
            `;
        }
    });

    // Función para llenar el menú de selección de comunas según la región seleccionada
    region.addEventListener("change", function() {
        // Lógica para llenar el menú de selección de comunas según la región seleccionada
    });

    // Función para validar los datos del formulario
    function validarFormulario() {
        // Lógica para validar los campos del formulario
        return true; // Retorna true si la validación pasa, de lo contrario false
    }

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
});
