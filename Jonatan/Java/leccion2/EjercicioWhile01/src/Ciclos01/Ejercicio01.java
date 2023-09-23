/*
Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir
el proceso hasta que se introduzca un numero negativo
*/
package Ciclos01;

import javax.swing.JOptionPane;//inportamos JOptionPane

public class Ejercicio01 {
    public static void main(String[] args) {

        
        int numero, cuadrado; // declaramos variables
        //JOptionPane abre una ventana emergente
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));//entrada de dato
        while(numero >= 0){//ciclo while, si es menor a 0 se cierra el ciclo
            cuadrado = (int)Math.pow(numero, 2);//La función Math.pow() devuelve la base elevada al exponente , esto es, baseexponente.
            System.out.println("El numero " +numero+" elevado al cuadrado es: "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
            
        }
        
        System.out.println("El programa a finalizado por numero negativo");
        
        
        
    }
    
}
