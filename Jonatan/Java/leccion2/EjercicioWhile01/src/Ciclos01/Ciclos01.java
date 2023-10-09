/*
Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir
el proceso hasta que se introduzca un numero negativo
*/

package Ciclos01;

import java.util.Scanner;


public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);//Clase scanner
        
        int numero, cuadrado; // declaramos variables
        System.out.println("Digite un numero: ");//pedimos al usuario un numero
        numero = Integer.parseInt(entrada.nextLine());//entrada de dato
        while(numero >= 0){//ciclo while, si es menor a 0 se cierra el ciclo
            cuadrado = (int)Math.pow(numero, 2);//La función Math.pow() devuelve la base elevada al exponente , esto es, baseexponente.
            System.out.println("El numero " +numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            
        }
        
        System.out.println("El programa a finalizado por numero negativo");
        
    }
}
