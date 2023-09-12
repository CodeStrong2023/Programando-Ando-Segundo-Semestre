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
