//Ampliamos el uso de var, let y const

/*
Con var podes areasignar en cualquier momento,
este foma parte del ambto global

un error es que se sobreescriba

*/

var nombre = 'Ariel';
nombre = 'Osvaldo';
console.log(nombre);
function saludar() {
    var nombre = 'Natalia';
    console.log(nombre);
}

console.log(nombre); // Aca no lee el dato en la funcino

if (true) {
    var edad = 34;
    console.log(edad);
}
console.log(edad); //en la funcion va correctament peo en el if fallo

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque, solo disponible dentro de un blque de llaves o
dentro de un funcion

*/


function saludar() {
    let nombre2 = 'Ariel';
    console.log(nombre2);
}

console.log(nombre2);

if (true) {
    var edad2 = 33;
    console.log(edad2);
}
console.log(edad2);

/* const se utiliza para valores constantes que no pueden ser reasignados */

//Ejercicio 1: Calcular estacion del anio
let mes = 4;
let estacion;

if (mes == 1 || mes == 2 || mes == 12) {
    estacion = "Verano";
}

else if (mes == 3 || mes == 4 || mes == 5) {
    estacion = "Otonio";
}

else if (mes == 6 || mes == 7 || mes == 8) {
    estacion = "Invierno";
}

else if (mes == 9 || mes == 10 || mes == 11) {
    estacion = "Primavera";
}
else {
    estacion = "Valor incorrecto"
}

console.log("El valor corresponde a la estacion de: " + estacion)

//Ejercicio 2: Hora del dia
/*
de 6 a 11 nos saluda: Good Morning

de 12 a 16 nos saluda: Good Morning

de 17 a 19 nos saluda: Good Morning

de 20 a 23 nos saluda: Good Morning

Trabajaremos con 24hrs
*/

let horaDia = 9;
let mensaje;
if (horaDia >= 6 && horaDia <= 11) {
    mensaje = "Good Morning"
}
else if (horaDia >= 12 && horaDia <= 16) {
    mensaje = "Good Afternoom"
}
else if (horaDia >= 17 && horaDia <= 19) {
    mensaje = "Good evening"
}
else if (horaDia >= 20 && horaDia <= 21) {
    mensaje = "Good night"
}
else {
    mensaje = "Valor Incorrecto"
}
console.log(mensaje)

//Estructura switch (la sintaxis es igual a JAVA)
switch (mes) {
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    
    case 3: case 4: case 5:
        estacion = "Otonio";
        break;
    
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor Incorrecto";
}
console.log("Bienvenido a la estacion de " + estacion)