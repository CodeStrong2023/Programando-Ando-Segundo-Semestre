//Ampliamos el uso de var, let y const
/*
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que se sobreescriba
*/

var nombre = "Antonio";
nombre = "Osvaldo";
console.log(nombre)

function saludar (){
    var nombre3 = "Natalia";
    console.log (nombre3);
}
//console.log(nombre3);//aqui no lee el dato en la funcion

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad);//en la funcion funciono correctamtnete, en la estructura if fallo

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque
solo dicponible dentro de un bloque de llaves
o dentro de una funcion
*/
function saludar2(){
    var nombre2 = "anto";
    console.log(nombre2);
}
//console.log(nombre2);

if (true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2020; una constante no puyede cambiar de valor
//console.log(fechaNacimiento);