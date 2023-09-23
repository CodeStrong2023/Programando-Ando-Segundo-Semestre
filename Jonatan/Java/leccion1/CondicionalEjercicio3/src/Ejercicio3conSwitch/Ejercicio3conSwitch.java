
package Ejercicio3conSwitch;

import java.util.Scanner;

public class Ejercicio3conSwitch {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un numero del 0 al 10: ");
        
        var calificacion = Integer.parseInt(entrada.nextLine());
        
        switch (calificacion) {
            case 10: case 9:
                System.out.println("Su Calificacion equivale a una A");
                break;
            case 8:
                System.out.println("Su Calificacion equivale a una B");
                break;
            case 7:
                System.out.println("Su Calificacion equivale a una C");
                break;
            case 6:
                System.out.println("Su Calificacion equivale a una D");
                break;
            case 5:
            case 4:
            case 3:
            case 2:
            case 1:
            case 0:
                System.out.println("Su Calificacion equivale a una F");
                break;
            default:
                System.out.println("Numero fuera de rango.");
                break;
        }
        
        
        
        
        
    }
    
}
