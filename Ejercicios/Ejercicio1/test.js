let n = 0; // contador

const suma = () => {
    const contador = document.getElementById("contador");
    n += 1;
    contador.textContent = n;
};

const resta = () => {
    const contador = document.getElementById("contador");
    n -= 1;
    contador.textContent = n;
};
//Funciones evento click
const sumButton = document.getElementById("btn-suma");
const resButton = document.getElementById("btn-resta");
sumButton.addEventListener("click", suma);
resButton.addEventListener("click", resta);
