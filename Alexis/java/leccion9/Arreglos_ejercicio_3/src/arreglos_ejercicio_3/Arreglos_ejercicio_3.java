/*
ejercicio 3: leer 5 numeros por teclado, almacenarlos en
un arreglo y a contiuacion realizar la media de los 
numeros positivos, la media de los negativos y contar el 
numero de ceros
 */
package arreglos_ejercicio_3;

import java.util.Scanner;

public class Arreglos_ejercicio_3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        float negativos = 0,positivos = 0,mediaNegativos = 0,mediaPositivos = 0;
        int conteo0=0, conteo_negativos = 0,conteo_positivos = 0;
        
        System.out.println("guardamos los elementos del arreglo: ");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1)+". digite un numero: ");
            numeros[i] = entrada.nextFloat();
            if(numeros[i]>0){
                positivos += numeros[i];
                conteo_positivos++;
            }
            else if(numeros[i]<0){
                negativos += numeros[i];
                conteo_negativos++;
            }
            else{
                conteo0++;
            }
 
        }
        if(conteo_positivos == 0){
            System.out.println("\nno se puede sacar la media de los numeros");
        }
        else{
            mediaPositivos = positivos/conteo_positivos;
            System.out.println("\nla media de los numeeros positivos es: "+mediaPositivos);
        }
        
        if(conteo_negativos == 0){
            System.out.println("\nno se puede sacar la media de los numeros");
        }
        else{
            mediaNegativos = negativos/conteo_negativos;
            System.out.println("\nla media de los numeeros positivos es: "+mediaNegativos);
        }
        
        System.out.println("la cantidad de ceros es: "+conteo0);
        
    }
    
}
