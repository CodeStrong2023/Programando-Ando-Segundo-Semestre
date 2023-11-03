/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package rectangulo;

import java.util.Scanner;

/**
 *
 * @author Silvio
 */
public class Rectangulo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
          Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese la base del rectangulo: ");
        double base = scanner.nextDouble();

        System.out.print("Ingrese la altura del rectangulo: ");
        double altura = scanner.nextDouble();

        double area = base * altura;
        double perimetro = 2 * (base + altura);

        System.out.println("El area del rectangulo es: " + area);
        System.out.println("El perimetro del rectangulo es: " + perimetro);
    
    }
    
}
