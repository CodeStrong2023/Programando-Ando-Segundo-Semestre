var nombre = 'Jose';
var apellido = 'Mendez';
var nombreCompleto = nombre+' '+apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Uriel'+' '+'Pardo';
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izquierda a derecha siguiendo la cadena asique lee el numero como string
console.log(juntos);
juntos = nombre + 78 + 17;
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre  += apellido;
console.log(nombre)

let nombre2 = 'Pedro'
console.log(nombre2);
const apellido2 = 'Lepes';
console.log(apellido2); //Una variable const no puede ser modificada

let x, y; //Se pueden crear variables dentro de una misma linea
x = 17, y = 21; //Se pueden designar varias variables en una misma linea
let z = x+y;
console.log(z);

