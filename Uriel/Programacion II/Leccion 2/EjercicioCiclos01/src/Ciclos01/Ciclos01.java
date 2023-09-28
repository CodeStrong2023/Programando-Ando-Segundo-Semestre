/*
Ejercicio 1: Leer un numero y mostrar su cuadrado,
repetir hasta ingresar un numero negativo
*/
package Ciclos01;

import java.util.Scanner;

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero, cuadrado;
        System.out.println("Digite un numero");
        numero = Integer.parseInt(sc.nextLine());
        while(numero >=0){
            cuadrado = (int) Math.pow(numero,2);
            System.out.println("El numero " +cuadrado+ " elevado al cuadrado es "+cuadrado);
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(sc.nextLine());
        }
        System.out.println("El programa ha finalizado por numero negativo");
    }
}
