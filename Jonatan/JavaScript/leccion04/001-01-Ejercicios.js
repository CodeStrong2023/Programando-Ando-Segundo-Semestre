//Ejercicio1: calcular estacion del anio

let mes = 4;
let estacion;

if(mes ==1 || mes == 2 || mes == 12){
    estacion = "Verano"
}
else if (mes == 3 || mes == 4 || mes == 5){
    estacion = "Otonio"
}
else if (mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno"
}
else if (mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera"
}
else{
    estacion = "Valor incorrecto"
}
console.log("El valor corresponde a al estacion de: "+estacion);

//Ejercico 2
/*
de 6 a 11 nos saluda good morning
de 12 a 16 nos saluda good afternoom
de 17 a 19 nos saluda good evening
de 20 a 23 nos saluda good night
trabajaremos con 24 Hs
*/

let horaDia = 9;
let mensaje;

if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Good morning"
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Good afternoom"
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good evening"
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good night"
}
else{
    mensaje = "Hora ingresada incorrecta"
}
console.log(mensaje);

switch(mes){
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion =  "otonio";
        break;
    case 6: case 7: case 8:
        estacion ="Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor incorrecto"
}
console.log("Bienvenido a la estacion de : "+estacion)