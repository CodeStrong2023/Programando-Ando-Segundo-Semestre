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