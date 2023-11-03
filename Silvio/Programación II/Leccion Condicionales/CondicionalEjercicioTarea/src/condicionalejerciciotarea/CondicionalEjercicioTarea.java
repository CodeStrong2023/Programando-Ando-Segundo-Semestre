/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package condicionalejerciciotarea;

import java.util.Scanner;

/**
 *
 * @author Fraggah
 */
public class CondicionalEjercicioTarea {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite la Nota Final: ");
        var calificacion = Integer.parseInt(entrada.nextLine());
        switch(calificacion){
            case 1: case 2: case 3: case 4: case 5:
                System.out.println("F");
                break;
            case 6:
                System.out.println("D");
                break;
            case 7:
                System.out.println("C");
                break;
            case 8:
                System.out.println("B");
                break;
            case 9: case 10:
                System.out.println("A");
                break;
        }     
    }
    
}
