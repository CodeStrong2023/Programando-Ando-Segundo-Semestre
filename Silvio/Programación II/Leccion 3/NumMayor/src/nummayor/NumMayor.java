/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package nummayor;

import java.util.Scanner;

/**
 *
 * @author Silvio
 */
public class NumMayor {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
         Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el primer numero: ");
        int numero1 = scanner.nextInt();

        System.out.print("Ingrese el segundo numero: ");
                
        int numero2 = scanner.nextInt();

        int mayor = (numero1 > numero2) ? numero1 : numero2;

        System.out.println("El mayor de los dos numeros es: " + mayor);
    }
    
}
