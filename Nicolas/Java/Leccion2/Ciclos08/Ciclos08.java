/* 
 * Ejercicio 8: Pedir un numero N, y mostrar todos los numeros
 */

import java.util.Scanner;

public class Ciclos08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
         
        int numero = Integer.parseInt(entrada.nextLine());
        int i = 1;
        while( i <= numero) {
            System.out.println(i);
            i++;
        }    
    }
}