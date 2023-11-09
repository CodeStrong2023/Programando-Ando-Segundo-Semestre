/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package salario;

import java.util.Scanner;

/**
 *
 * @author Silvio
 */
public class Salario {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
         Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese las horas semanales trabajadas: ");
        int horasTrabajadas = scanner.nextInt();

        System.out.print("Ingrese el salario por hora: ");
        double salarioPorHora = scanner.nextDouble();

        double salarioTotal = horasTrabajadas * salarioPorHora;

        System.out.println("El salario total del empleado es: " + salarioTotal);
        
    }
    
}
