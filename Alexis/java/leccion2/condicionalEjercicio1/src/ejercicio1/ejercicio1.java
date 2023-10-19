
package ejercicio1;

import java.util.Scanner;

public class ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite un mes del año:");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "estacion desconocida";
        if (mes == 1 || mes == 2 || mes == 3){
            estacion = "verano";
        }
        else if (mes == 4 || mes == 5 || mes == 6){
            estacion = "otoño";
        }
        else if (mes == 7 || mes == 8 || mes == 9){
            estacion = "invierno";
        }
        else if (mes == 10 || mes == 11 || mes == 12){
            estacion = "primavera";
        }
        System.out.println("estacion = " + estacion);
        
        
        
        
        
        
        
    }
}
