/*
Ejercicio 1: Leer 5 numeros, guardarlos en un arreglo y 
mostrarlos en el mismo orden introducidos.
*/
package arreglos_ejercicio_1;

import java.util.Scanner;


public class Arreglos_Ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numeros[] = new int[5];
        for (int i= 0; i<5; i++){
        System.out.println("Introduzca 5 numeros: ");
        numeros[i] = Integer.parseInt(entrada.nextLine());
            System.out.println("numero"+i+" = "+numeros[i]);
        }
        
        
    }
}
