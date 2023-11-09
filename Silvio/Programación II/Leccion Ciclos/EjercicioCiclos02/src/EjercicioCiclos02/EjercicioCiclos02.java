/*
 Ejercicio 2: Leer un numero, indicar si es positivo o negtivo.
El proceso se reptira hasta que se ingrese el 0
 */
package EjercicioCiclos02;

import java.util.Scanner;

public class EjercicioCiclos02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite un  numero");
        var numero = Integer.parseInt(sc.nextLine());
        while(numero != 0){
            if (numero > 0) {
                System.out.println("El numero " +numero+ " es positivo");
            }
            else{
                System.out.println("El numero " +numero+ " es negativo");
            }
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(sc.nextLine());
        }
        System.out.println("El numero "+numero+" finaliza el programa");
    }
}
