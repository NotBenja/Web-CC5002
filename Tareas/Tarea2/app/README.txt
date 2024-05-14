Decisiones de diseño:

-Validación frontend:
1. Como la lista de frutas y verduras solo aparece al momento de seleccionar el tipo de producto,
en la validación js solo se corrobora que haya al menos un tipo de producto seleccionado.
2. La validación de la región y comuna solo revisará que el campo haya seleccionado una opción para cada una,
pues como las opciones vienen de la base de datos, no es necesario revisar más. Lo mismo aplica para producto.

Validación backend:
1. Ya que las opciones para seleccionar producto, región y comuna vienen directamente de la base de datos, 
entonces sus validaciones serán true siempre y cuando no sean "none".

