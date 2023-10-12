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