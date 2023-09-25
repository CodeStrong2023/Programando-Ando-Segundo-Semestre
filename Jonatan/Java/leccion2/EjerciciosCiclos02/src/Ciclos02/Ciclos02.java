/*
Ejercicio2: Leer un numero e indicar si es positivo o negativo. El proceso
se repetira hasta que se introduzca un 0
*/
package Ciclos02;

import java.util.Scanner;//clase scanner



public class Ciclos02 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);//clase escaner
        System.out.println("Digite un Numero");//pedimos al usuario un numero
        var numero = Integer.parseInt(entrada.nextLine());//ingresamos
        while(numero != 0 ){//ciclo while si es igual a 0 se termina el programa
            if(numero > 0){//si el numero es positivo a 0 se
                System.out.println("El numero "+numero+" es POSITIVO");
            }
            else{
                System.out.println("El numero "+numero+" es NEGATIVO");
                
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        
        System.out.println("El numero "+numero+" finaliza el programa");
      
        
        
        
    }
    
}
