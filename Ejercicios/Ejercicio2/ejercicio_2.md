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
Un ataque XSS es un tipo de ataque por injección, donde se insertan scripts de manera maliciosa dentro de una página que se ve segura y confiable. El propósito que tiene es afectar al usuario final de la aplicación web, el cual no tiene cómo saber que está interactuando con un script malintencionado, ya que piensa que es parte de el mismo sitio. Mediante XSS, el atacante puede acceder a informacion sensible, ya sean cookies o session-tokens. <br>
Este tipo de ataque podría ser prevenido realizando una correcta validación de los inputs que existen dentro de la aplicación web, de esta forma se evita la inserción de código malicioso. Es importante proteger todas las variables que interactúen con el usuario mediante validación, pues es la forma más eficiente de protegerse de un XSS. Muchos frameworks facilitan este proceso, pues ayudan a mantener las variables protegidas.<br> 
Este ataque es especialmente peligroso en sitios donde se maneja información muy sensible como aplicaciones web de bancos, pues si no se validan los inputs de manera correcta, un atacante podría insertar código malicioso para obtener datos de usuarios que posean cuentas bancarias en el sitio. De esta forma, se podrían conseguir números de tarjeta, saldos de cuenta, entre otros. Por lo tanto, es de vital importancia que los inputs sean siempre validados de manera correcta, pues así se evita que nuestra aplicación sea vulnerable a este tipo de ataques.

## Pregunta 2
Como se mencionó en auxiliar, existen varias herramientas que se pueden utilizar para programar aplicaciones web más complejas que las que hemos visto en el curso. Esta pregunta busca que ud. investigue 3 librerías de javascript o *frameworks* de front-end y describa sus principales características, ventajas, desventajas y ejemplos de uso. Finalmente, indique cuál de las tecnologías presentadas utilizaria para implementar su página web personal y por qué.

**Nota:** Se espera que ud. escriba un breve resumen de cada tecnología, seguido de al menos 2 ventajas y 2 desventajas de cada una.

**Respuesta**:
