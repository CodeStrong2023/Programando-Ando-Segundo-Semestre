//Tipos de datos en JS
/*
Tipos de comentarios lineal o por parrafo
*/
var nombre = 'Uriel'; //Tipo str
console.log(nombre);

nombre = 7;
console.log(nombre);
console.log(typeof nombre);

nombre = 12.3;
console.log(nombre);
console.log(typeof nombre);

var numero = 3000; //Tipo numerico
console.log(numero);

var objeto = { //Tipo Objeto
    nombre : "Uriel",
    apellido : "Pardo",
    edad : 27,
    telefono : "2604121212"
}
console.log(objeto);

//Tipo de dato boolean
var bandera = true;
console.log(bandera);

//FUnciones son tipos de datos y se pueden reutilizar llamando en repetidas ocasiones
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo)

//Tipo de dato Clase
class Persona{
    constructor(nombre, apellido){
        this.nombre;
        this.apellido;
    }
}
console.log(Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);
x = undefined;
console.log(x);

//nul : significa ausencia de valor, esta vacio
var y = null; //null no es un tipo de dato pero su origen es object
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford'];
console.log(autos);
console.log(typeof autos);

//Datos vacios Empty
var z = ''; //Es una cadena vacia
console.log(z);
console.log(typeof z);