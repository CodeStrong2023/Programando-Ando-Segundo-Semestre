
package ciclos10;

import java.util.Scanner;

/*
Ejercicio 10: Perdir 10 numeros y escribir la suma total
Hocerlo con la clase Scanner y JOptionPane
 */
public class Ciclos10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;
        for(int i = 1; i <= 10; i++){
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma += numero;
        }
        System.out.println("\nLa suma de todos los numeros es: "+ suma);
    }
}
