// Ejercicio para encontrar numeros pares e impares
let parImpar = 10;
if(parImpar % 2 == 0) {
    console.log("Es un numero Par");
}
else{
    console.log("Es un numero IMPAR");
}

// Ejercicio: es mayor de edad
let edad = 20, adulto = 18;
if( edad >= adulto){
    console.log("Es una persona adulta");
}
else{
    console.log("Es una persona menor de edad");
}

// Ejercicio: Dentro de un rango
let dentroRango = 5; // Aqui vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if( dentroRango >= valMin && dentroRango <= valMax) {
    console.log("Esta dentro del rango establecido")
}
else {
    console.log("No esta dentro del rango")
}

//Ejercicio : Si el padre puede asistir al juego de su hijo
let vacaciones = true, diaDescanso = true;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre No puede asistir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2) 
let numero = 9;
resultado2 = numero % 2 == 0 ? "es Par" : "es Impar";
console.log(resultado2)

// Convertir String a Number
let miNumero = "10"; // Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero); // Esta es una funcion
console.log(typeof edad2);
//Funcion isNaN
if(isNaN(edad2)){ //No es un numero = is Not a Number (devuelve un resultado booleano)
    console.log("Esta variable no contiene solo numeros")
}
else{
    



    if(edad2 >= 18){
        console.log("Puede votar");
    }
    else{
        console.log("No puede votar, es menor de edad");
    }
}
let resultado3 = edad2 >= 18 ? "Puede votar" : "No puede votar, es menor de edad";
console.log(resultado3)

