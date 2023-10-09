
package Ejercicio6;

import java.util.Scanner;


public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo, luis, juan, total;
        System.out.println("Ingrese la cantidad d edinero de Guillermo");
        guillermo= Float.parseFloat(entrada.nextLine());
        
        luis = guillermo / 2;
        juan = (luis + guillermo) / 2;
        total = luis + guillermo + juan;
        System.out.println("El dinero de Luis es: U$$"+luis);
        System.out.println("El dinero de Juan es: U$$"+juan);
        System.out.println("El total de dinero entre los tres es de: U$$"+ total);
    }
}
