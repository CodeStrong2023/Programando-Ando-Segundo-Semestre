/*
 Ejercicio 12: Pedir un numero y calcular el factorial de un numero. Hacerlo con clase Scanner y clase JOptionPane
 */
package ciclos12;

import java.util.Scanner;

public class Ciclos12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int factorial = 1;
        System.out.println("Digite el numero a calcular el factorial");
        int numero = Integer.parseInt(sc.nextLine());
        for (int i= 1; i<=numero; i++){
            factorial *= i;
        }
        System.out.println(numero+"!= "+factorial);
    }
}
