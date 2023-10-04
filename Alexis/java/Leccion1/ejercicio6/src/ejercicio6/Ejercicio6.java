package ejercicio6;

import java.util.Scanner;

public class Ejercicio6 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo, luis, juan, total;
        System.out.println("digite la cantindad de dinero de Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis = guillermo / 2;
        juan = (luis + guillermo)/ 2;
        total = luis + guillermo + juan;
        System.out.println("el dinero de Luis es $"+luis);
        System.out.println("el dinero de Juan es $"+juan);
        System.out.println("el total de  dinero entre los tres es $"+total);
    }

}
