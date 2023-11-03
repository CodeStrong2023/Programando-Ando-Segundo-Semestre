/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio6;

import java.util.Scanner;

/**
 *
 * @author Silvio
 */
public class Ejercicio6 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese la cantidad de dinero de Guillermo: $");
        double dineroGuillermo = scanner.nextDouble();

        double dineroLuis = dineroGuillermo / 2;
        double dineroJuan = (dineroGuillermo + dineroLuis) / 2;

        System.out.println("Cantidad de dinero de Guillermo: $" + dineroGuillermo);
        System.out.println("Cantidad de dinero de Luis: $" + dineroLuis);
        System.out.println("Cantidad de dinero de Juan: $" + dineroJuan);

        double totalDinero = dineroGuillermo + dineroLuis + dineroJuan;
        System.out.println("Cantidad total de dinero entre los 3: $" + totalDinero);
    }
    
}
