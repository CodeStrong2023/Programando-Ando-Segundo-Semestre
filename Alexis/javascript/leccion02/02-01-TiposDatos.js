// tipos de datos en javascscript

/*
la sintaxis en lo que es comentarios
es muy similar a la de java
realmente diriamos que es identica
*/

var nombre = "ariel"; // tipo str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

var numero = 3000; // tipo numerico
console.log(numero);

var objeto = {
    nombre : "ariel",
    apellido : "betancut",
    telefono : "12345678"
}
console.log(objeto);

// tipos de datos boolean
var bandera = true;
console.log(bandera);

//tipo de dato funcion
function miFuncion(){}
console.log(miFuncion);

//tipo de dato symbol
var simbolo = Symbol("mi simbolo");
console.log(simbolo);

//tipo de dato clase
class persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof persona);

//tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x)

// null: significa ausencia de valor
var y = null; // null no es un tipo de dato, pero su origen es object
console.log(typeof y);

//tipo de dato array y empty string
var autos = ["citroen","audi","BMW","ford"];
console.log(autos);
console.log(typeof autos) //preguntamos que tipos de datos es:

var z = "";
console.log(z); //esto se refiere a que es una cadena vacia:
console.log(typeof z)





