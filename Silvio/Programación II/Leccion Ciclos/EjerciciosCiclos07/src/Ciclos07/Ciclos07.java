/*
Ejercicio 7; Pedir numeros hasta que se ingrese uno negativo calcular la media
*/
package Ciclos07;

import java.util.Scanner;

public class Ciclos07 {
    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite un numero");
        numero = Integer.parseInt(sc.nextLine());
        while(numero >= 0){
            suma += numero;
            conteo++;
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(sc.nextLine());
        }
        if(conteo == 0){
            System.out.println("Error. La division por cero no existe");
        }
        else{
            promedio = (float)suma/conteo;
            System.out.println("El promedio es "+promedio);
        }
    }
}
