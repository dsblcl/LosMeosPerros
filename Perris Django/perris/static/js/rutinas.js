function mensaje(){
    alert('Hola Mundo');
}
function formulario(){
    var nombre=document.getElementById("txtNombre").value;
    var rut=document.getElementById("txtRun").value;
    var largo=rut.length;
    if (largo!=8) {
        alert("rut mal ingresado");
        return;
    }
    var suma=0;var mult=3;
    for (var index = 0; index < 8; index++) {
        var caracter=rut.substring(index,index+1);
        suma=suma+(parseInt(caracter)*mult);
        mult--;
        if (mult==1) {
            mult=7;
        }        
        
    }
    alert("suma:"+suma);    
    alert("Digito:"+(11-(suma % 11)));
}