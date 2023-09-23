//String
var nombre = 'Silvio';
console.log(nombre);
nombre = 7; //puede cambiar de tipo
console.log(typeof nombre);

nombre = 12.3;
console.log(typeof nombre);

//Numerico
var numero = 5555666;
console.log(numero);

var objeto = {
    nombre: "Silvio",
    apellido: "Stefanucci",
    telefono: "3463442455"
}
console.log(typeof objeto);

//Boolean
var bandera = true;
console.log(bandera);

// Funcion
function miFuncion() {
    
}
console.log(miFuncion);

//Simbolo
var simbolo = Symbol("Simbolo");
console.log(typeof simbolo);

//Clase
class Persona {
    constructor(nombre, apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);

//Undefined
var x;
console.log(typeof x);

//Null
var y = null; // null no es un tipo de dato pero su origen es object
console.log(typeof y);

//Array
var autos = ['Chevrolet', 'Astra', 'Aston Martin', 'Ferrari'];
console.log(autos);
console.log(typeof autos);

//Empty String
var z = '';
console.log(z);
console.log(typeof z);
