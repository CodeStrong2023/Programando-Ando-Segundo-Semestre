
package ciclos12;

import java.util.Scanner;

/*
 Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con las dos Clases, Scanner y JOptionPane
 */
public class Ciclos12 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        long factorial =1;
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(entrada.nextLine());
        for(int i = 1; i<= numero; i++){
            factorial *= i;
        }
        System.out.println("\nEl factorial del numero ingresado es: " + factorial);
    }
}
