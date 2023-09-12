
package Cliclos4;

import java.util.Scanner;

/**
 Ejercicio 4
 * Pedir numeros hasta que se teclee uno negattivo y mostrar cuantos numeros se han introducido.
 * primero con la clase scanner y luego JOptionPane
 * 
 */
public class Ciclos4 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            
            System.out.println("El numero " +numero + " es Positivo" );
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Ha ingresado" +conteo + " numero que no son negativos" );
    }
}
