//Ejercicio 1: Calcular estacion del año

let mes = 3;
let estacion;
if(mes==12 || mes == 1 || mes == 2){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if (mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto, los meses van del 1 al 12";
}
console.log("La estacion correspondiente al mes "+mes+" es: "+estacion);


switch(mes){
    case 12: case 1: case 2:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valo incorrecto";
}
console.log("La estacion correspondiente al mes "+mes+" es: "+estacion);

//Ejercicio 2: Hora del dia
let hora = 23.5;
let estado;
if(hora <= 7 && hora>=0){
    estado = "Descansando";
}
else if (hora > 7 && hora<8){
    estado = "Aseo persoanl y desayuno";
}
else if(hora >= 8 && hora <= 16){
    estado = "Trabajo con pausa para almorzar";
}
else if (hora > 16 && hora < 17){
    estado = "Aseo personal";
}
else if(hora>=17 && hora <19){
    estado = "Descanso y/o tareas varias";
}
else if(hora >= 19 && hora <=23){
    estado = "Cursado sincronico o asincronico";
}
else if(hora>23 && hora < 23.99){
    estado = "Cena y aseo personal";
}
else{
    estado = "Hora incorrecta";
}
console.log("En esa hora el estado de la persona es: "+estado)