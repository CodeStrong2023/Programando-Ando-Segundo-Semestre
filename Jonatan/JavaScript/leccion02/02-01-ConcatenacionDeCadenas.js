var nombre = 'Jose';
var apellido = "Mondelez";
var nombreCompleto = nombre+' '+apellido;//primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Bentancud';//segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219;//lee de izq a derecha siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 17;
console.log(juntos); //se concatena pero no se suma. sigue siendo de modo string
nombre += apellido //Tercera Concatenacion usando el operador simplificado
console.log(nombre);
let nombre2 = "Pedrito"//hoy ya no se usa var, se usar let y const
console.log(nombre2);
const apellido2 = "Lepesinio";
//apellido2 = "Perez"; una constantte no puede ser modificada
console.log(apellido2);

let x,y; //se Puede crear varias variabl;es dentro de una misma linea
x = 17, y = 21; //se puede hacer asignacion dentro de una misma linea
let z = x + y;//se asigna el valor d ela operacion
console.log(z);

//una variable no debe tener un numero delante de el nombre

let _1num = 31;
let $break = "Rompe";//no se utilizan palaras reservadas

console.log(_num1);
console.log($break);