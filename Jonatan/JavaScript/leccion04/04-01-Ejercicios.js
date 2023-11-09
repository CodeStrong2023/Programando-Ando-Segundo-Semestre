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

//Evitar repetir tu codigo
//Dry don't repeat yourself

let days = 1;
switch(days){
    case 1:
        console.log('Hoy es Lunes.');
        break;
    case 2:
        console.log('Hoy es Martes.');
        break;
    case 3:
        console.log('Hoy es Miercoles.');
        break;
    case 4:
        console.log('Hoy es Jueves.');
        break;
    case 5:
        console.log('Hoy es Viernes.');
        break;  
    case 6:
        console.log('Hoy es Sabado.');
        break;
    case 7:
        console.log('Hoy es Domingo.');
        break;
    default:
        console.log("Error en el ingreso del dia de la semana")
        break;

}

//Esta es la vercion Mejorada

let days2 = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'];

function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('Out of Range')
    }
    return days2[n-1];
}
console.log(getDay(5));

//Ejercicio MEses del anio con switch y con opcion Mejorada
let month = 13;
switch(month){
    case 1:
        console.log('Es Enero.');
        break;
    case 2:
        console.log('Es Febrero.');
        break;
    case 3:
        console.log('Es Marzo.');
        break;
    case 4:
        console.log('Es Abril.');
        break;
    case 5:
        console.log('Es Mayo.');
        break;
    case 6:
        console.log('Es Junio.');
        break;
    case 7:
        console.log('Es Julio.');
        break;
    case 8:
        console.log('Es Agosto.');
        break;
    case 9:
        console.log('Es Septiembre.');
        break;
    case 10:
        console.log('Es Octubre.');
        break;
    case 11:
        console.log('Es Noviembre.');
        break;
    case 12:
        console.log('Es Diciembre.');
        break;
    default:
        console.log('Mes del anio erroneo.')
}

let month2 = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diembre']
function getMonth(n){
    if(n < 1 || n > 12){
        throw new Error('Out of Range');
    }
    return month2[n-1];
}
console.log(getMonth(1));