//ejercicio 1: calcular estacion del año
let mes = 4;
let estacion;
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "primavera";
}
else{
    estacion = "valor incorrecto"
}
console.log("el valor corresponde a la estacion de: "+estacion)
//ejercicio 2: hora del dia
let horaDia = 9;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "good morning";
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "good afternoom";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "good evening";
}
else if(horaDia >= 20 && horaDia <= 1623){
    mensaje = "good night";
}
else{
    mensaje = "valor incorrecto";
}
console.log(mensaje)

//estructura switch(la sintaxis es igual a Java)
switch(mes){//no solo se pueden utilizar numero, tambien cadenas
    case 1: case 2: case 12:
        estacion = "verano";
        break;
    case 3: case 4: case 5:
        estacion = "otoño";
        break;
    case 6: case 7: case 8:
        estacion = "invierno";
        break;
    case 9: case 10: case 11:
        estacion = "primavera";
        break;
    default:
        estacion = "valor incorrecto"
}
console.log("bienvenido a la estacion de: "+estacion)

//evitar repetir tu codigo
//dry don't repeat yourself
//let days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
let days = 6;
switch (days){
    case 1:
        console.log('hoy es lunes')
        break;
    case 2:
        console.log('hoy es martes')
        break;
    case 3:
        console.log('hoy es miercoles')
        break;
    case 4:
        console.log('hoy es jueves')
        break;
    case 5:
        console.log('hoy es viernes')
        break;
    case 6:
        console.log('hoy es sabado')
        break;
    case 7:
        console.log('hoy es domingo')
        break;
    default:
        console.log('error en el ingreso del dia del dia de la semana')
        break;

}

//esta es la version mejorada
let days2 = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out of range');
    }
    return days2[n-1];
}
console.log(getDay(5));

//hacer un ejercicio similar al que esta hecho, pero ahora con los 
//meses del año, debes hacerlo con la estuctura switch y lugo con 
//la funcion en la opcion mejorada

let month = 11;
switch (month){
    case 1:
        console.log('es enero')
        break;
    case 2:
        console.log('es febrero')
        break;
    case 3:
        console.log('es marzo')
        break;
    case 4:
        console.log('es abril')
        break;
    case 5:
        console.log('es mayo')
        break;
    case 6:
        console.log('es junio')
        break;
    case 7:
        console.log('es julio')
        break;
    case 8:
        console.log('es agosto')
        break;
    case 9:
        console.log('es septiembre')
        break;
    case 10:
        console.log('es octubre')
        break;
    case 11:
        console.log('es noviembre')
        break;
    case 12:
        console.log('es diciembre')
        break;
    default:
        console.log('error en el ingreso del mes del año')
        break;

}

//esta es la versio mejorada

let month2 = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'sptiembre', 'octubre', 'noviembre', 'diciembre']
function getMonth(n){
    if(n < 1 || n > 12){
        throw new Error('out of range');
    }
    return month2[n-1]
}
console.log(getMonth(1))








