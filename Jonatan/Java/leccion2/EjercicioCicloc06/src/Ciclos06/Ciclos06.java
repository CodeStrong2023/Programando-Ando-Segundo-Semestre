/*
Ejercicio 6 : Pedir numeros hasta que se teclee un 0
mostrar la suma de todos los numeros introducidos.
*/



package Ciclos06;

import java.util.Scanner;

public class Ciclos06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);//iniciamos la clase Scanner
        int numero,suma;//Declaramos las variables necesarias
        suma = 0;//iniciamos acumulador suma en 0
        
        do{//ciclo while que primero verifica la condicion y luego inicia el codigo
            System.out.println("Digite un numero");
            numero = Integer.parseInt(entrada.nextLine());
            suma += numero;
         }while(numero != 0);//si numero ingresado por el usuario es difrente a 0 se acumula el numero y se vuelve a pedir, de lo contrario termina el ciclo y suma todos los numeros
        System.out.println("\nLa suma de todos los numeros ingresados es : "+suma);// mostramos el valor acumulado al usuario
    }
}
    
