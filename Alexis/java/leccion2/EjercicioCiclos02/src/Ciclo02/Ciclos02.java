/*
ejercicio 2: leer un numero e indicar si es positivo o
negativo. el proceso se repetira hasta que se introdusca 
un cero 0
hacer este ejercicio on la clase scanner,
luego hacerlo nuevamente con la clase JoptionPane
 */
package Ciclo02;

import java.util.Scanner;


public class Ciclos02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if (numero > 0){
                System.out.println("el numero "+numero+" es POSITIVO");
            }
            else{
                System.out.println("el numero "+numero+" es NEGATIVO");
            }
            System.out.println("digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("el numero "+numero+" finaliza el programa");
            
        
        
        
        
        
        
        
    }
}