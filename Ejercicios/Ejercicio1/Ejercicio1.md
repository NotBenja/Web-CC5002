# Ejercicio 1

**Nombre**: Benjamín Reyes Bravo

---
## Consideraciones
- Este ejercicio se debe realizar de manera individual.
- Puede usar internet, sus apuntes y cualquier material que desee siempre y cuando las respuestas esten escritas en sus propias palabras.
- Se encuentra **totalmente prohibido** utilizar modelos generativos del lenguaje tales como ChatGPT para resolver este ejercicio. Por medio de un software especializado, se revisará que su solución no haya sido plagiada. Aquellas entregas que presenten evidencia de plagio serán calificadas con la nota mínima.


## Pregunta 1
Explique por que el realizar validaciones del input del usuario en el front-end es una caracteristica pero no una medida de seguridad. 

**Respuesta**: Las validaciones a los input de usuarios sí son una característica, pues tienen como principal propósito evitar el mal uso de formularios, como por ejemplo, enviando notificaciones de esto a los usuarios indicando que existen errores en su input en caso de no pasar la validación. Sin embargo, las validaciones no son medidas de seguridad, debido a que no protegen realmente a la aplicación web, pues incluso poseyendo validaciones, se puede acceder al código fuente de la página y realizar técnicas maliciosas que puedan esquivar dicha validación y así vulnerar nuestra aplicación.

## Pregunta 2
Usted cuenta con el siguiente codigo HTML:
```html
<div>
    <p>Contador: <span id="contador">0</span></p>
    <button type="button" id="btn-resta">-1</button>
    <button type="button" id="btn-suma">+1</button>
</div>
```
Implemente un contador bidireccional utilizando la plantilla disponible mas abajo, solo programe donde se le indica. Se espera que tras apretar un boton, el contador se actualice sin la necesidad de recargar la pagina. **No esta permitido modificar el HTML**.

**Respuesta**:
```js
let n = 0; // contador

const suma = () => {
    //Llamamos al contador en el html según su ID
    const contador = document.getElementById("contador");
    n += 1;
    //Actualizamos el contador
    contador.textContent = n;
};

const resta = () => {
    //Análogo a suma()
    const contador = document.getElementById("contador");
    n -= 1;
    contador.textContent = n;
};
//Funciones evento click

//Llamamos a los botones del documento html según sus ID's respectivas
const sumButton = document.getElementById("btn-suma");
const resButton = document.getElementById("btn-resta");
//Definimos que al hacer "click" en dichos botones hay que llamar a las funciones ya definidas para cada caso.
sumButton.addEventListener("click", suma);
resButton.addEventListener("click", resta);


```
