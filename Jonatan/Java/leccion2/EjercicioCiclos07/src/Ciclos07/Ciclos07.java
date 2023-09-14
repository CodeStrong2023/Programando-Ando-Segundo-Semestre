/*
Ejercicio N7: pedir numeros hasta que se introduzca uno negativo
y calcular el promedio
*/
package Ciclos07;

import java.util.Scanner;//importamos la clase scanner

public class Ciclos07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;//declaramos e iniciamos las variables
        float promedio = 0;
        
        System.out.println("Digite un numero");
        numero = Integer.parseInt(entrada.nextLine());
        while( numero >= 0){//mientras el numero no sea negativo
            suma += numero;//sumamos los numeros que ingresa el usuario
            conteo++;//conteo de los numeros
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
        }
        if(conteo == 0){
            System.out.println("\nError, la divicion entre cero no existe");  
        }
        else {
            promedio = (float)suma/conteo;
            System.out.println("\nEl promedio es: "+promedio);
        }
    }
    
}
