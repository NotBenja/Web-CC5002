# Ejercicio 4: "*Unrestricted File Upload*"

**Nombre**: Benjamín Reyes Bravo

--- 
## Introduccion
Hemos enfatizado la importancia de ser extremadamente cautelosos en el manejo de la entrada de los usuarios, incluyendo los archivos. De hecho, la vulnerabilidad [*Unrestricted File Upload*](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload), la cual corresponde a confiar plenamente en los archivos subidos por el usuario, puede tener consecuencias catastróficas.

El objetivo de este ejercicio es comprender bien las posibles **consecuencias** de un manejo de archivos "mediocre" y las formas de **prevenirlas**.

### Pregunta 1
Investigue y explique **con sus propias palabras** 3 posibles ataques que un usuario malicioso podria realizar a una aplicacion web con la vulnerabilidad *Unrestricted File Upload*". Se espera que para cada ataque se mencionen las **consecuencias** del mismo.

**Respuesta:**

1. Un posible ataque sería la carga de archivos maliciosos que contegan código ejecutable, lo cual permitiría que el atacante pueda ejecutar comandos en el servidor.Lo anterior tiene graves consecuencias, como la toma del control total del sistema, el robo de datos, entre otros. Un ejemplo de esto sería que el atacante suba un archivo shell.py que contenga el siguiente código:
```python
import os
os.system(input("Enter command: "))
```


2. Otro posible ataque sería el almacenamiento de scripts XSS. En este caso, cuando un usuario accede a la aplicación e interactúa de alguna forma con el archivo, este comenzaría a ejecutarse y realizaría acciones maliciosas. Este tipo de código XSS puede venir incluído en archivos SVG y HTML, por lo que es importante evitar su subida al servidor. Las consecuencias de que un usuario abra el archivo malicioso pueden ir desde el robo de cookies de sesión hasya la suplantación de identidad, entre otros.

3. Por último, otro tipo de ataque sería el de desbordamiento de almacenamiento. Este ataque consiste en que el atacante sube varios archivos de gran peso en un bucle continuo, para así llenar el almacenamiento del servidor de la app web. 
Una consecuencia de este tipo de ataque es que los usuarios no puedan acceder a la aplicación y también que los servicios dependientes del almacenamiento se vean afectados.

* [*Fuente de las respuestas anteriores*](https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload) 

### Pregunta 2
Ahora que ya tenemos claro que descuidar el manejo de archivos es peligroso, les pedimos listar 5 metodos preventivos para esta vulnerabilidad.

**Respuesta:**

1. Validación y restricción de tipos de archivo: Se deben implementar validaciones que permitan tipos específicos y rechazar el resto. Para esto se tienen que verificar MIME types, las extensiones y el contenido de los archivos, todo con el fin de corroborar que el archivo es del tipo que se espera. Cabe destacar que esto no necesariamente es suficiente para evitar la subida de archivos maliciosos.

2. Uso de software antivirus: Se utilizan antivirus para escanear malwares y analizar los archivos que se quieran subir al servidor.

3. Renombramiento de archivos y directorios no ejecutables: Se cambia el nombre de los archivos subidos y se almacenan en directorios que no sean ejecutables, de esta forma se evita la ejecución de los scripts maliciosos que puedan contener.

4. Limitar el número y tamaño de archivos: Se establecen estos límites para evitar ataques que puedan desbordar el almacenamiento del servidor de la aplicación.

5. Autenticación y autorización estrictos: Se debe asegurar que aquellos usuarios que estén autenticados y autorizados sean los únicos con permisos para subir archivos.