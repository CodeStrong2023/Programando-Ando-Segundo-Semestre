/*
Ejercicio 10:
Pedir 10 numeros y escribir la suma total
*/
package ciclos10;

import java.util.Scanner;

public class Ciclos10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int numero, suma =0;
        for(int i = 1; i<=10; i++){
            System.out.println("Digite un numero");
            numero = Integer.parseInt(sc.nextLine());
            suma += numero;
        }
        System.out.println("\nLa suma de todos los numeros es: "+suma);
    }
}
