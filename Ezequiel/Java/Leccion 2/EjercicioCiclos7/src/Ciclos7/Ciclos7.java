
package Ciclos7;

import java.util.Scanner;

/**
Pedir numeros hasta que se introduzca un negativo y calcular la media
 */
public class Ciclos7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0, conteo = 0;
        float promedio = 0;

        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine()); 
        while(numero >= 0){
           suma += numero;
           conteo++;
           System.out.println("Digite otro numero");
           numero = Integer.parseInt(entrada.nextLine());
        }
        if(conteo == 0){
            System.out.println("Error, la division entre cero no existe");
        }else{
            promedio = (float)suma/conteo;
            System.out.println("El promedio es: " +promedio);
        }

    }
}
