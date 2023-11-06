/*
Ejercicio 3: Leer 5 numeros por teclado, almacenarlos en
un arreglo y a continuacion realizar la media de los
numeros positivos, la media de los negativos y contar
el numero de ceros.
*/
package arreglos_ejercicio_3;

import java.util.Scanner;


public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        float suma_negativos= 0, suma_positivos= 0, mediaNegativos, mediaPositivos;
        int conteo0=0, conteo_negativos=0, conteo_positivos=0;
        
        
    
        for(int i=0 ; i<5 ; i++) {
            System.out.println((i+1)+"Ingrese un numero: ");
            numeros[i] = entrada.nextFloat();
            
            if(numeros[i]>0) {
                suma_positivos += numeros[i];
                conteo_positivos++;
            }
            else if(numeros[i]<0){
                suma_negativos += numeros[i];
                conteo_negativos++;
            }
            else{
                conteo0++;
            }
        }
        
        if(conteo_positivos ==0) {
            System.out.println("No se ingresaron numeros positivos");
            
        }
        else{
            mediaPositivos = suma_positivos/conteo_positivos;
            System.out.println("La media de los positivos es: "+mediaPositivos);
            
        }
        
        if(conteo_negativos == 0){
            System.out.println("No se ingresaron numeros negativos");
            
        }
        else {
            mediaNegativos = suma_negativos/conteo_negativos;
            System.out.println("La media de los negativos es: "+mediaNegativos);
        }
        
        if(conteo0 == 0) {
            System.out.println("No se ingresaron numeros de valor 0");
        }
        
        else{
            System.out.println("La cantidad de numeros con valor 0 ingresados fue: "+conteo0);
        }
        
        
        
        
        
    
    
    
    }
}
