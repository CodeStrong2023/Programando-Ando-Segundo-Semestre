//Comentario de una sola linea
/*Comentario
de
muchas lineas */

var nombre = 'ezequiel';//tipo string
console.log(nombre);
nombre = 7;
console.log(typeof nombre);

nombre = 12.3;
console.log(typeof nombre);

var numero = 10923431; //tipo numerico
console.log(numero);

var objeto = {
    nombre: "Ezequiel",
    apellido: "Lorenz",
    telefono: "12312414"
}

console.log(typeof objeto);

// tipo de datos boolean
var bandera = true;
console.log(bandera);

//  funciones son tipos de datos

function miFuncion() {
    
}
console.log(miFuncion);

// dato symbol

var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

// Tipo da dato Clase

class Persona {
    constructor(nombre, apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(Persona);

// Tipo de dato undefined

var x;
console.log(typeof x);

//null: Significa ausencia de valor

var y = null; // null no es un tipo de dato pero su origen es object

console.log(typeof y);

// Tipo de dato array

var autos = ['Citroen', 'Audi', 'BMW', 'Ford'];
console.log(autos);
console.log(typeof autos);

// Empty String

var z = '';
console.log(z);
console.log(typeof z);
