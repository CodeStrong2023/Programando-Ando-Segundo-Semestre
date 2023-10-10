var nombre = "jose";
var apellido = "montes";
var nombreCompleto = nombre+" "+apellido; //primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = "ariel"+" "+"betancut"; //segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //lee de izq a der siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + (78 + 17); //aqui se puede diferenciar a travez de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //tercera concatenacion usando el operador simplificado
console.log(nombre);

// hoy ya no se usa var, se utilizajet y const
let nombre2 = "pedro";
console.log(nombre2);

const apellido2 = "lepes";
//apellido2 = "peres"; una constanto no puede ser modificada
console.log(apellido2);

let x, y; //se puede crear varias varaibles dentro de una misma linea
x = 17, y = 21; //se puede hacer asignacion de varias variables dentro de la misma linea
let z = x + y;
console.log(z);

let _1num = 31; //no utilizar numeros para iniciar el nombre de una variable
let rompiendo = "rompe"; //noutilizar palabras reservadas para vaiables

console.log(_1num);
console.log(rompiendo);


