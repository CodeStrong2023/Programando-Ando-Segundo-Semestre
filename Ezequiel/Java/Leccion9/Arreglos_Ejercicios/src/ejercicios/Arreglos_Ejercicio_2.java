
package ejercicios;

import java.util.Scanner;

/*
Ejericio 2: Leer 5 numeros, guardarlos en un arreglo y mostrarlos
en el orden inversio al que fueron introducidos
 */
public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];

        System.out.println("Guardando los datos de un arreglo");
        for(int i = 0;i<5; i++){
            System.out.println((i+1)+". Digite un numero");
            numeros[i] = entrada.nextFloat();
        }

        System.out.println("\nImprimir los elementos del arreglo");
        for(int i = 4;i>=0; i--){
            System.out.println(i+" "+numeros[i]);
        }
        
        System.out.println("\n");
        
    }
    
    
}
