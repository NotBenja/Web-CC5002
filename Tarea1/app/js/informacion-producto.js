let fotoProducto = document.getElementById("fotoProducto");
let size = 0;
fotoProducto.addEventListener("click", function(){
    if(size==1){
        size = 0
        fotoProducto.src = "../../media/big/manzana_big.jpg"
    }else if(size == 0){
        size = 1
        fotoProducto.src = "../../media/medium/manzana_medium.jpg"
    }
})