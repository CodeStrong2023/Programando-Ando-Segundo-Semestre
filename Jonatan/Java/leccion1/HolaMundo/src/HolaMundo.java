
import java.util.Scanner;


public class HolaMundo {

    public static void main(String[] args) {
        /* System.out.println("Hola Mundo desde Java");
        
        //tipos de variables enteros
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        
        //tipos de variables string
        String miVariableCadena = "Bienvenidos a  la Tecnicatura";
        System.out.println(miVariableCadena);
        miVariableCadena = "A seguir Practicando papaaa!";
        System.out.println(miVariableCadena);
         */

        //var inferencia de tipos en java
        /*var miVariableEntera2 = 10;
       var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //con soutv + tab copia el sout anterior
        //para ejecutar rapidamente Shift + 6
        
        //reglar para definir una Variable en JAVA//
        /*1 primer caracter podemos usar cualquier letra del alfabeto, por 
        conveccion usar camelcase en minuscula*/
        //2 no se puede usar numeros al comienzo de la variable
        //3 no puede tener caracteres especiales
        //4 puede tener _ y $ al comienzo pero no es tan comun
        /*5 usar acentos, se pueden pero no es recomendable ya que no estamos 
        acostumbrados a poner todas las variables con acento */
        //6 prohibido usar el # es un caracter ilegal
        //ejercicio concatenacion
        //var usuario = "Miguel";
        /*var titular = "Mecanico";
        var union = titular + " " + usuario;
        System.out.println("union = " + union);*/
        //var a = 8;
        // var b = 4;
        // System.out.println(usuario + "  " + (a + b));
        //si la primer variable son de distintos tipos no se suma solo se va
        //a concatenar, tenemos que separar entre parentecis.
        /*var nombre = "Marta";
        System.out.println("\n Nueva linea: \n" + nombre); //diagonal inversa y N para salto de linea
        System.out.println("Tabulador:\t" + nombre);// con \t hacemos un espacio
        System.out.println("\t \t.:MENU:.");//EJEMPLO se puede poner varios\t
        System.out.println("Retroceso:     \b" + nombre); //caracter de retroceso 
        System.out.println("Comillas simples: \'" + nombre + "\'"); //pone con comillas simples la variable
        System.out.println("Comillas Dobles : \"" + nombre + "\"");//pone en comila dobles
         
        //clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su Nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el Titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);

        EJERCICIO DEL LIBRO
        
        Scanner entrada = new Scanner (System.in);
        System.out.println("Ingrese el titulo del Libro: ");
        var titulo = entrada.nextLine();
        System.out.println("Proporciona el autor: ");
        var autor = entrada.nextLine();
        System.out.println( titulo + " Fue escrito por " + autor);
        
        //CLASE 4
        byte numEnteroByte = 127;
        System.out.println("numEnteroByte =" + numEnteroByte);
        System.out.println("Valor minimo del Byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: "+ Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort ="+ numEnteroShort);
        System.out.println("Valor minimo del Short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: " + Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt =" + numEnteroInt);
        System.out.println("Valor minimo del Int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int: " + Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong =" + numEnteroLong);
        System.out.println("Valor minimo del Long: " + Long.MIN_VALUE);
        System.out.println("Valor maximo del Long: " + Long.MAX_VALUE);
                
        float numFloat = 3.4028235E38F;
        System.out.println("numFloat =" + numFloat);
        System.out.println("Valor minimo del Float: " + Float.MIN_VALUE);
        System.out.println("Valor maximo del Float: " + Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble =" + numDouble);
        System.out.println("Valor minimo del Double: " + Double.MIN_VALUE);
        System.out.println("Valor maximo del Double: " + Double.MAX_VALUE);
        
        //CLASE 5 TIPOS PRIMITIVOS EN JAVA PARTE 2
        //INFERENCIA DE TRIPOS VAR y TIPOS PRIMITIVOS
        
        var numEntero = 20; //las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = "+ numEntero);
        var numFloat = 10.0F; //Automaticamente con el punto se transforma en tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        
        //Tipo primitivos CHAR (solo almacena un caracter y se hace con comillas simples
        char miVariableChar = 'a';
        System.out.println("miVariableChar = "+miVariableChar);
        //caracter unicode
        char varCaracter = '\u0024';//indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter = "+varCaracter);
        
        char varCaracterDecimal = 36;
        System.out.println("varCaracterDecimal = "+ varCaracterDecimal);
        
        char varCaracterSimbolo = '$';
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        //
        
        var varCaracter1 = '\u0024';//indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter1 = "+varCaracter1);
        
        var varCaracterDecimal1 = (char)36; //hacemos la convercion para que tome el tipo char
        System.out.println("varCaracterDecimal1 = "+ varCaracterDecimal1);
        
        var varCaracterSimbolo1 = '$';//un caracter especial, se puede copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        //
        
        int varEnteroChar = '$';//nos muestra el valor decimal al simbolo (36)
        System.out.println("varEnteroChar = " + varEnteroChar);
        
        int caracterChar = 'b';//valor decimal 98 en juego de caracteres unicode
        System.out.println("caracterChar =" + caracterChar);
        
        //CLASE 6 (TIPOS PRIMITIVOS PARTE 3)
        
        //Conversion de tipos parte 1
        var edad = Integer.parseInt("20"); //convertimos un dato string a int
        System.out.println("edad = " + (edad + 1)); //sumamos +1 a el 20 convertido a string
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("ValorPI= " + valorPI);
        
        //pedir un valor
        var entrada = new Scanner(System.in);//el in significa que trabajaremos con la consola
     // System.out.println("Digite su edad: ");
     // edad = Integer.parseInt( entrada.nextLine());//convertimos string a int con parseINT
     // System.out.println("edad = " + edad);
        
        //conversion de tipos primitivos en JAVA parte 2
        
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(3);//nos muetra la posicion del indice de la cadena string
        System.out.println("fraseChar = " +fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = "+ fraseChar);
        */
        
        
        
        
    }

}
