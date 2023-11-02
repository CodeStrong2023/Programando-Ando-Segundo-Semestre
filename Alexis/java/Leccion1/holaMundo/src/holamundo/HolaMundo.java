import java.util.Scanner;

public class holaMundo {

    public static void main(String[] args) {
        /* System.out.println("hola mundo desde java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable=5;
        System.out.println(miVariable);
        //Tipo String
        String miVariableCadena="Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programacion";
        System.out.println(miVariableCadena);
         */

        //Var - inferencia de tipos en Java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + tab
        //para ejecutar shift + f6 es la tecla para mayuscula
        //reglas para definir una variable en java
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;*/
 /* System.out.println("union = " + union);
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));
        //ejercicio: caracteres especiales
        var nombre = "Natalia";
        System.out.println("nueva linea: \n" + nombre);//diagonal inversa y letra n
        System.out.println("tabulador: \t" + nombre);
        System.out.println("\t\t.:MENU:.");//tabulador es un espacio para centrar
        System.out.println("retoceso: \b\b"+nombre);//caracter de retroceso
        System.out.println("comillas simples: \'"+nombre+"\'");
        System.out.println("comillas dobles: \""+nombre+"\"");*/
        //clase scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("escriba el titulo: ");
        var titulo2=entrada.nextLine();
        System.out.println("resultado: "+titulo2+" "+usuario2);*/
 /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("valor minimo del byte: " + Byte.MIN_VALUE);
        System.out.println("valor maximo del byte: " + Byte.MAX_VALUE);
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("valor minimo del short: " + Short.MIN_VALUE);
        System.out.println("valor maximo del short: " + Short.MAX_VALUE);
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("valor minimo de int: " + Integer.MIN_VALUE);
        System.out.println("valor maximo de int: " + Integer.MAX_VALUE);
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("valor minimo de long: " + Long.MIN_VALUE);
        System.out.println("valor maximo de long: " + Long.MAX_VALUE);*/
 /*float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("el valor minimo de Float: " + Float.MIN_VALUE);
        System.out.println("el valor maximo de Float: " + Float.MAX_VALUE);
        double numDouble=1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("el valor minimo de Double: " + Double.MIN_VALUE);
        System.out.println("el valor maximo de Double: " + Double.MAX_VALUE);*/
 /*var numEntero=20; //Las literales sin punto autamaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat=10.0F; //automaticamente con el punto se trasforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
        //tipos primitivos char
        /*char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);

        char varCaracter = '\u0024';//indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterdecimal = 36;//valor decimal del juego de caracter unicode
        System.out.println("varCaracterdecimal = " + varCaracterdecimal);
        char varCaracterSimbolo = '$';//un caracter especial, copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);

        var varCaracter1 = '\u0024';//indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterdecimal1 = (char) 36;//valor entero y asigna tipo int
        System.out.println("varCaracterdecimal1 = " + varCaracterdecimal1);
        var varCaracterSimbolo1 = '$';//un caracter especial, copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);

        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);*/
 /*//tipos primitivos tipos booleanos
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        if (varBool){
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("la bandera es roja");
        }
        
        //algoritmo: es mayor de edad?
        var edad = 30; //literal tener presente la inferencia de tipos
        //var adulto = edad>=18; //esta es una expresion Booleana
        if (edad >= 18){
            System.out.println("eres mayor de edad");
        }
        else {
            System.out.println("eres menor de edad");
        }*/
        //conversion de tipo primitivo
        /*var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        //pedir un valor
        var entrada = new Scanner(System.in);
        System.out.println("dijite su edad:");
        edad = Integer.parseInt(entrada.nextLine());
        System.out.println("entrada = " + entrada);*/
        //conversion de tipos primitivos en java parte 2
        /*var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(0);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("dijite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);*/
 /*int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion);
        solucion = num1 - num2;
        System.out.println(" solucion de la resta = " + solucion);
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);
        var solucion2 = 3.4/num2;
        System.out.println("solucion2 resultado de la division= " + solucion2);
        
        solucion = num1 % num2; //guarda el residuo de la solucion
        System.out.println("solucion2 = " + solucion2);//5/4
        if (num1 % 2 ==0)
            System.out.println("es un numero par");
        else
            System.out.println("es un numero impar");*/
 /*int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2; //una operacion
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1; //varNum1 = varNum1 + 1
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 -= 2;
        System.out.println("varNum2 = " + varNum2);
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        varNum3 /= 4;
        System.out.println("varNum3 = " + varNum3);
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);*/
        // operadore unarios: cambio de signos
        /*var varA = 7; 
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);// el resultado sera un numero negativo
        
        //operador de negacion
        var varC = true; //esta literal por defaul en java es de tipo boolean
        var varD = !varC; //aqui esta invirtiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        // operadores unarios de incremento: Preincremento
        var varE = 9;// se va a modificar su valor
        var varF = ++varE; //simbolo antes de la variable
        //primero se incremanta la variable y despues se usa su valor
        System.out.println("varE = " + varE);//se incrementa en la unidad
        System.out.println("varF = " + varF);//va a sumar uno
        
        //posincremento
        var varG = 3;
        var varH = varG++;//primero el valor de la varible, luegoel incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //operadores unarios de decremento: predecremento
        var varI = 4;
        var varJ =--varI;
        System.out.println("varI = " + varI);//la variable ya esta con decremento
        System.out.println("varJ = " + varJ);
        
        //posdrecemento
        var varK = 8;
        var varL =varK--;
        System.out.println("varK = " + varK);//aqui va a decrementar en 1
        System.out.println("varL = " + varL);
        
        //operadores de igualdad y reacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("bNum = " + bNum);
        
        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "hello";
        var cadenaB = "bye bye";
        var cadenaC = cadenaA == cadenaB;
        System.out.println("cadenaC = " + cadenaC);
        
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);
        
        var gVar = aNum >= bNum;//> >= < <= == !=
        System.out.println("gVar = " + gVar);
        
        if (aNum % 2 == 0){
            System.out.println("el numero es par");
        }else {
            System.out.println("el numero es impar");
        }
            
        var edad = 30;
        var adulto = 18;
        if (edad >= adulto){
            System.out.println("es mayor de edad");
        }
        else{
            System.out.println("es menor de edad");
        }*/
 /*var valorA = 7;
        var valorMnimo = 0;
        var valorMaximo = 10;
        var respuesta= valorA >= 0 && valorA <= 10;
        if (respuesta)
            System.out.println("esta dentro del rango establecido");
        else
            System.out.println("esta fuera del rango establecido");
        
        var vacaciones = false;
        var diaLibre = false;
        if (vacaciones || diaLibre)
            System.out.println("papá puede asistir al juego de su hijo");
        else
            System.out.println("papá no puede asistir al juego de hijo");*/
        //operador ternario
        /*var resultadoT = (5 > 4) ? "verdadero" : "falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "es par" : "es impar";
        System.out.println("resultadoT = " + resultadoT);*/
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);//6
        System.out.println("y = " + y);//9
        System.out.println("z = " + z);

        var solucionArimetica = 4 + 5 * 6 / 3;//4 + ((5 * 6) / 3 = 10 + 4 = 14
        System.out.println("solucionArimetica = " + solucionArimetica);

        solucionArimetica = (4 + 5) * 6 / 3;//4 + 5 = 9 * 6 = 54 / 3 = 18
        System.out.println("solucionArimetica = " + solucionArimetica);
    }
}