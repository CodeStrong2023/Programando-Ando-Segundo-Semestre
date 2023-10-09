var nombre = "Ariel"; //Tipo String
console.log(nombre);
var nombre = 7;
console.log(typeof nombre);


var numero = 3000; //Tipo Numerico
console.log(numero);

var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2604088892"

}

console.log(objeto);


// Tipo de Dato Boolean
var bandera = true;
console.log(bandera);

// Tipo de Dato Funcion
function miFuncion (){}
console.log(typeof miFuncion);

// Tipo de Dato Symbol
var simbolo = Symbol("Mi Simbolo");
console.log(typeof simbolo);

// Tipo de Dato Clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

// Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

// null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es object
console.log(typeof y);

// Tipo de dato array y Empty String
var autos = ["Citroen", "Audi,", "BMW", "Ford"];
console.log(autos);
console.log(typeof autos);  //Preguntamos que tipo de dato es:

var z = "";
console.log(z); //Esto se refiere a que es una cadena vacia:
console.log(typeof z);
