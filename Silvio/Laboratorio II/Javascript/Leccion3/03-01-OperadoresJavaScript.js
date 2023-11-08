//Ejercicio para encontar numeros pares
let parImpar = 5;
if (parImpar % 2 == 0) {
    console.log("Es un numero PAR");
}
else {
    console.log("Es un numero Impar");
}


//Ejerciio: es mayorr d eedad
let edad = 20, adulto = 18;
if (edad >= adulto) {
    console.log('Usted es una eprsona adulta');
}
else {
    console.log('Euste es una persona menor de edad')
}

//ejercicio dentro de un rango

let dentroRango = 5; //aca se va a ir cambiando el valor
let valMin = 0, valMax = 10;
if (dentroRango >= valMin && dentroRango <= valMax) {
    console.log('Esta dentro del rango establecido')
}
else {
    console.log('Esta fuera del rango establecido')
}

//Ejercicio si el padre puede asistir al juego de su hijo
let vacacioens = false, diaDescanso = false;
if (vacaciones || diaDescanso) {
    console.log("El padre puede asistir al juego de su hijo");
}
else {
    console.log("El padre NO puede asistir al juego de su hijo");
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)

//Convertir de String a Number
let miNumero = "10";
console.log(miNumero);
let edad2 = Number(miNumero);
console.log(edad2);

//Funcion isNaN

if (isNaN(edad2)) {
    console.log("esta variable no contiene solo numeros");
}

if (edad2 >= 18) {
    console.log("puede votar");
}
else {
    console.log("uy joven para votar");
}

let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar"