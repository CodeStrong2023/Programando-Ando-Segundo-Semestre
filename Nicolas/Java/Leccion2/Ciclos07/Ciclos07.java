/*
 * Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo
 * y calcular la media
 */

import java.util.Scanner;

public class Ciclos07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero = 0, conteo = 0, suma = 0;
        float promedio = 0;
        System.out.println("Digite un numero: ");
        while(numero >= 0) {
            suma += numero;
            conteo++;
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        if(conteo==0){
            System.out.println("\nError, La division entre cero no existe");
        }
        else{
            promedio = (float)suma/conteo;
            System.out.println("\nEl promedio es: "+promedio);
        }        

    }
 }