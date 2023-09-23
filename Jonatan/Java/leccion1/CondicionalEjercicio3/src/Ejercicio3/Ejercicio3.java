
package Ejercicio3;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero entre 0 y 10: ");
        var calificacion = Integer.parseInt(entrada.nextLine());
        if (calificacion >= 9 && calificacion <= 10){
            System.out.println("Su Calificacion equivale a una A");
        }
        else if (calificacion >= 8 && calificacion <9){
            System.out.println("Su Calificacion equivale a una B");
        }
        else if (calificacion >= 7 && calificacion <8){
            System.out.println("Su Calificacion equivale a una C");
        }
        else if (calificacion >= 6 && calificacion <7){
            System.out.println("Su Calificacion equivale a una D");
        }
        else if (calificacion >= 0 && calificacion <6){
            System.out.println("Su Calificacion equivale a una F");
        }
        else{
            System.out.println("Numero fuera de rango.");
        }
        
        
        
        
        
        
        
        
        
    }
}
