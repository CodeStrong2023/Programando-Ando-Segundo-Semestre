/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio5;

import java.util.Scanner;

/**
 *
 * @author Silvio
 */
public class Ejercicio5 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
         Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese la primera calificacion: ");
        double calificacion1 = scanner.nextDouble();

        System.out.print("Ingrese la segunda calificacion: ");
        double calificacion2 = scanner.nextDouble();

        System.out.print("Ingrese la tercera calificacion: ");
        double calificacion3 = scanner.nextDouble();

        double sumaCalificaciones = calificacion1 + calificacion2 + calificacion3;

        System.out.println("La suma de las calificaciones es: " + sumaCalificaciones);
    }
    
}
