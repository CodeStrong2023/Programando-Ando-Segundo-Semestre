/*
Ejerciico 8:

pedir un numero N a usuario y mostrar todos los numeros desde
el 1 al N
*/
package Ciclos8;

import java.util.Scanner;

public class Ciclos8 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(entrada.nextLine());
        int i = 1;
        
        while(i <= numero){
            System.out.println(i);
            i++;
        }
    }
}
