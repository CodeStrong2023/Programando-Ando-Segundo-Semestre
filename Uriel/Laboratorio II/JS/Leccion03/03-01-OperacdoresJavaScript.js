//Ejercicio para encontrar numeros pares
let parImpar = 1;
if(parImpar % 2 == 0){
    console.log("Es un numero par");
}
else{
    console.log("Es un numero impar");
}

//Ejercicio: mayor de edad 
let edad = 14, adulto = 18;
if(edad >= adulto){
    console.log("Es una persona adulta");
}
else{
    console.log("No es una persona adulta");
}

//Ejercicio: dentro d un rango
let dentroRango = 11;
let min = 0, max = 10;
if(dentroRango >= min && dentroRango <= max){
    console.log("Esta dentro del rango establecido");
}
else{
    console.log("No esta dentro del rango");
}

//Ejercicio: si el padre puede assustir al juego de su hijo
let vacaciones = false, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre No puede asistir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3>2 ? "Verdadero" : "Falso";
console.log(resultado2)
let numero = 10;
resultado2 = numero % 2 == 0 ? "Es un numero par" : "Es un numero impar"
console.log(resultado2)

//Convertir String a Number
let miNumero = "18";
console.log(typeof miNumero);
let edad2 = Number(miNumero);
console.log(typeof edad2)

if(isNaN(edad2)){
    console.log("Esta variable no es un numero")
}
else{
    if(edad2 >= 18){
        console.log("Puede votar");
    }
    else{
        console.log("No puede votar");
    }
}


let resultado3 = edad2 >= 18 ? "Puede votar" : "No puede votar";
console.log(resultado3);

//Funcion isNaN
