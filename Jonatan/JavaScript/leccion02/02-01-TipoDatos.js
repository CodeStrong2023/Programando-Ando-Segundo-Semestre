//Tipos de datos en JavaScript
/*
La sintacis en lo que es comentarios
es muy similar a la de java
realmente diriamos que es identica
*/
//Dato String STR
var nombre = 'Jona';
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
//dato de tipo numerico
var numero = 10;
console.log(typeof numero);
//dato de tip Objet
var objeto ={
    nombre : "Ariel",
    Apellido: "Betancud",
    Telefono: "260567654"
}
console.log(objeto);

//tipo de dato BOOLEAN "bandera" True o False

var bandera = false;
console.log( bandera);

//tipo de dato Funcion
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato Symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//tipo de dato CLASE"Constructor"
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(Persona);

//tipo de dato undefined
var x;
console.log(x);

//null : significa ausencia de valor
var y = null;//null no es un tipo de dato, pero su origen es de tipo objet
console.log( null)

//tipo de dato array y empy String(cadena vacia)
var autos = ['Citroen','Audi','BMW','Ford'];
console.log(autos);
console.log(typeof autos);//preguntamos que tipo de datos es

var z = '' ;//cadena vacia
console.log(z);
console.log(typeof z);