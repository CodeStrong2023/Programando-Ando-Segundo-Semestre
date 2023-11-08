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

let days = 'Sábado';

switch (days) {
    case 'Lunes':
        console.log('Hoy es ' + days);
        break;
    case 'Martes':
        console.log('Hoy es ' + days);
        break;
    case 'Miércoles':
        console.log('Hoy es ' + days);
        break;
    case 'Jueves':
        console.log('Hoy es ' + days);
        break;
    case 'Viernes':
        console.log('Hoy es ' + days);
        break;
    case 'Sábado':
        console.log('Hoy es ' + days);
        break;
    case 'Domingo':
        console.log('Hoy es ' + days);
        break;
    default:
        console.log('Día no válido');
}

let today = new Date();
let dayOfWeek = today.getDay();

let dayName;
switch (dayOfWeek) {
    case 0:
        dayName = "Domingo";
        break;
    case 1:
        dayName = "Lunes";
        break;
    case 2:
        dayName = "Martes";
        break;
    case 3:
        dayName = "Miércoles";
        break;
    case 4:
        dayName = "Jueves";
        break;
    case 5:
        dayName = "Viernes";
        break;
    case 6:
        dayName = "Sábado";
        break;
    default:
        dayName = "Día desconocido";
        break;
}

console.log("Hoy es " + dayName);


let days2 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];

function getDay(n) {
    if (n < 1 || n > 7) {
        throw new Error('out of range');
    }
    return days2[n - 1];
}

console.log(getDay(5));

/*
Hacer un ejercicio similar al que esta hecho, pero ahora con los meses del anio, 
debes hacerlo con la estructura switch y luego con la funcion en la opcion mejorada

*/

let month = 'Enero';

switch (month) {
    case 'Enero':
        console.log('Este mes es ' + month);
        break;
    case 'Febrero':
        console.log('Este mes es ' + month);
        break;
    case 'Marzo':
        console.log('Este mes es ' + month);
        break;
    case 'Abril':
        console.log('Este mes es ' + month);
        break;
    case 'Mayo':
        console.log('Este mes es ' + month);
        break;
    case 'Junio':
        console.log('Este mes es ' + month);
        break;
    case 'Julio':
        console.log('Este mes es ' + month);
        break;
    case 'Agosto':
        console.log('Este mes es ' + month);
        break;
    case 'Septiembre':
        console.log('Este mes es ' + month);
        break;
    case 'Octubre':
        console.log('Este mes es ' + month);
        break;
    case 'Noviembre':
        console.log('Este mes es ' + month);
        break;
    case 'Diciembre':
        console.log('Este mes es ' + month);
        break;
    default:
        console.log('Mes no válido');
}


let months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

function getMonth(n) {
    if (n < 1 || n > 12) {
        throw new Error('Fuera de rango');
    }
    return months[n - 1];
}

console.log(getMonth(3)); // Esto imprimirá "Marzo"

