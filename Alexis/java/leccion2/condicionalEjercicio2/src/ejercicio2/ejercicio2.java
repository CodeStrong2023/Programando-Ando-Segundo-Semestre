
package ejercicio2;

import java.util.Scanner;

public class ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite un numero del mes");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "estacion desconocida";
        switch (mes){
            case 1: case 2: case3:
                estacion = "verano";
                break;
            case 4: case 5: case6:
                estacion = "otoño";
                break;
            case 7: case 8: case9:
                estacion = "invierno";
                break;
            case 10: case 11: case12:
                estacion = "primavera";
                break;
        }
        System.out.println("estacion = " + estacion);
        
        
        
        
        
    }
}
