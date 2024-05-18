let tabla = document.getElementById("tablaPedidos");
for (let i = 1; i < tabla.rows.length; i++) {
  let fila = tabla.rows[i];
  fila.addEventListener("click",function(){
    window.location.href = "../pedido/informacion-pedido.html";
  })   
  }
