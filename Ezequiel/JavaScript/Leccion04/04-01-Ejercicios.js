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