# Ejercicio 2
**Nombre**: Benjamín Reyes Bravo

---

## Observaciones
Tenga en cuenta las siguientes observaciones al realizar el ejercicio:

- El ejercicio es de carácter **personal**; la copia será penalizada con **nota mínima**.
- De ser necesario investigar, usted esta **autorizado a utilizar internet** como herramienta. Sin embargo, **debe citar** toda fuente que utilice para responder las preguntas.
- El uso de modelos generativos de lenguaje como **ChatGPT está estrictamente prohibido** y será penalizado con **nota mínima**

## Pregunta 1

¿Qué es el ataque de "Cross Site Scripting" (XSS) y cómo podría prevenirse? Describa un escenario en el cual este tipo de ataque podría ser especialmente peligroso. Para responder esta pregunta, puede basarse en [este articulo de la OWASP](https://owasp.org/www-community/attacks/xss/).

**Respuesta**:
Un ataque XSS es un tipo de ataque por injección, donde se insertan scripts de manera maliciosa dentro de una página que se ve segura y confiable. El propósito que tiene es afectar al usuario final de la aplicación web, el cual no tiene cómo saber que está interactuando con un script malintencionado, ya que piensa que es parte de el mismo sitio. Mediante XSS, el atacante puede acceder a informacion sensible, ya sean cookies o session-tokens, entre otros. <br>
Este tipo de ataque podría ser prevenido realizando una correcta validación de los inputs que existen dentro de la aplicación web, de esta forma se evita la inserción de código malicioso. Es importante proteger todas las variables que interactúen con el usuario mediante validación, pues es la forma más eficiente de protegerse de un XSS. Muchos frameworks facilitan este proceso, pues ayudan a mantener las variables protegidas.<br> 
Este ataque es especialmente peligroso en sitios donde se maneja información muy sensible como aplicaciones web de bancos, pues si no se validan los inputs de manera correcta, un atacante podría insertar código malicioso para obtener datos de usuarios que posean cuentas bancarias en el sitio. De esta forma, se podrían conseguir números de tarjeta, saldos de cuenta, entre otros. Por lo tanto, es de vital importancia que los inputs sean siempre validados de manera correcta, pues así se evita que nuestra aplicación sea vulnerable a este tipo de ataques.

## Pregunta 2
Como se mencionó en auxiliar, existen varias herramientas que se pueden utilizar para programar aplicaciones web más complejas que las que hemos visto en el curso. Esta pregunta busca que ud. investigue 3 librerías de javascript o *frameworks* de front-end y describa sus principales características, ventajas, desventajas y ejemplos de uso. Finalmente, indique cuál de las tecnologías presentadas utilizaria para implementar su página web personal y por qué.

**Nota:** Se espera que ud. escriba un breve resumen de cada tecnología, seguido de al menos 2 ventajas y 2 desventajas de cada una.

**Respuesta**:
<div>
<div>Los frameworks que mencionaré a continuación los escogí porque son los más populares actualmente, y por lo que he investigado, cada uno posee sus ventajas al momento de utilizarlos, por lo que en la explicación de cada uno se listan dichos beneficios, como también sus contras. Además, me interesan porque otorgan muchas posibilidades al momento de armar el front-end de una aplicación web.</div>
<h1> 1. React.js </h1>
<div> React es una biblioteca de Javascript para construir interfaces de usuario. Es popular por su enfoque en componentes reutilizables y un DOM virtual que permite actualizaciones óptimas.</div>

<div>Ventajas:</div>
<li>DOM Virtual: Permite actualizaciones eficientes y rápidas de la interfaz de usuario al cambiar solo las partes que necesitan ser actualizadas.</li>
<li>Componentes Reutilizables: Facilita la creación de interfaces avanzadas y su mantenimiento debido a la arquitectura basada en componentes.</li>

<div>Desventajas:</div>
<li>Curva de Aprendizaje: Difícil de entender al principio para los nuevos desarrolladores.</li>
<li>Solo es una Librería: Requiere de otras herramientas para realizar funciones como el enrutamiento y la gestión del estado.</li>
</div>

<div>
<h1> 2. Angular.js </h1>
<div>Angular es un framework de desarrollo front-end basado en TypeScript elaborado por Google. Ofrece una estructura completa para aplicaciones SPA (Single-Page Applications) y PWA (Progressive Web Apps), con características como enlace de datos bidireccional y un sistema de inyección de dependencias. Angular es más utilizado para proyectos grandes y complejos. </div>

<div>Ventajas:</div>
<li>Estructura Completa: Ofrece una solución completa con herramientas para desarrollar aplicaciones más complejas.</li>
<li>Two-Way Data Binding: Facilita la sincronización entre vista y modelo.</li>

<div>Desventajas:</div>
<li>Complejidad: Su gran cantidad de funciones puede resultar tedioso para aumentar la complejidad del proyecto.</li>
<li>Rendimiento: Puede ser más lento comparado con otros frameworks debido a su tamaño y complejidad.</li>
</div>

<div>
<h1> 3. Vue.js </h1>
<div>Vue es un framework utilizado para construir interfaces de usuario. Está diseñado para ser usado incrementalmente y es fácil de integrar con otros proyectos. Vue se centra en la capa de visualización y es capaz de levantar aplicaciones de una sola página más avanzadas cuando se usa con otras herramientas y librerías complementarias. </div>

<div>Ventajas:</div>
<li>Integración Gradual: Se puede integrar fácilmente con proyectos ya existentes o usar para construir aplicaciones complejas desde cero.</li>
<li>Documentación Clara: Posee una documentación bien escrita y comprensible, haciendo que sea más fácil de aprender.</li>
<div>Desventajas:</div>
<li>Comunidad Más Pequeña: Su comunidad es más pequeña en comparación con React o Angular, pero está en crecimiento.</li>
<li>Riesgos de Flexibilidad: Su flexibilidad puede llevar a errores en el código si no se siguen normas para evitarlos.</li>


</div>


<h2>Fuentes de información</h2>

<li><a href="https://kinsta.com/es/base-de-conocimiento/que-es-react-js/">React</a></li>
<li><a href="https://openwebinars.net/blog/que-es-angular-2021/">Angular</a></li>
<li><a href="https://es.vuejs.org/v2/guide/">Vue</a></li>
<li><a href="https://www.rootquotient.com/blog/top-10-frontend-frameworks-2023/">Info general1</a> 
<a href="https://stackdiary.com/front-end-frameworks/">Info general2</a>
<a href="https://medium.com/@dunyan/react-the-pros-and-cons-of-a-popular-javascript-library-6e1e443a3e22">Info general3</a>
</li>

