*La carpeta extras dentro del .zip contiene los archivos sql entregados por el equipo docente
y algunas fotos para testear la insercion de fotos en la base de datos.

Decisiones de diseño:

-Página de estadísticas:
Para acceder a los gráficos se implementó un botón que dice ¨Estadísticas¨ en la navbar, el cual lleva a una página permite elegir cuál
gráfico se visualizar.

-Validación frontend:
1. Como la lista de frutas y verduras solo aparece al momento de seleccionar el tipo de producto,
en la validación js solo se corrobora que haya al menos un tipo de producto seleccionado.
2. La validación de la región y comuna solo revisará que el campo haya seleccionado una opción para cada una,
pues como las opciones vienen de la base de datos, no es necesario revisar más. Lo mismo aplica para producto.

Validación backend:
1. Ya que las opciones para seleccionar producto, región y comuna vienen directamente de la base de datos, 
entonces sus validaciones serán true siempre y cuando no sean "none".

