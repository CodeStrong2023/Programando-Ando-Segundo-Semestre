//Ejercicio para Encontrar Numeros pares
let parInpar = 2;
if(parInpar % 2 == 0){
    console.log("Es un numero PAR");
}
else{
    console.log("Es un numero IMPAR");
}

//Ejercicio: es mayor de edad
let edad = 17;
if(edad >= 18){
    console.log("Usted es Mayor de Edad");
}
else{
    console.log("Usted es menor de edad.");
}

//Ejercicio: Dentro de un Rango

let dentroRango = 7;
let valMin = 0; valMax = 10;
if( dentroRango >= valMin && dentroRango <= valMax){
    console.log("Esta dentro del Rango")
}
else{
    console.log("Esta fuera del Rango.")
}
//Ejercicio: si el paddre puede asistir al juego de su hijo 
let vacaciones = true, diaDescanso = false;
if (vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo.")
}
else{
    console.log("El padre no puede asistir al juego de su hijo.")
}

//Operador Ternario(se usa para codigos cortos, para largos se recomienda if else)
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)

let numero = 9;
resultado2 = numero %2 == 0 ? "Es un numero PAR" : "Es un numero IMPAR";
console.log(resultado2)

//Convertir String a Number
let miNumero = "18";//cadena limpia, si tiene una letra genera errores
console.log(typeof miNumero);
let edad2 = Number(miNumero);//transformamos a number
console.log(typeof edad2);

//Funsion isNaN
if(isNaN(edad2)){//No es un numero = is Not a Number(devuelve un resultado booleano)
    console.log("Esta variable no contiene solo numeros")
}
else{
    if(edad2 >= 18){
        console.log("Puede Votar.");
    }
    else{
        console.log("Muy joven para Votar.")
    }
}


//operador ternario
let resultado3 = edad2 >= 18 ? "Puede Votar" : "Muy Joven para Votar";
console.log(resultado3);

