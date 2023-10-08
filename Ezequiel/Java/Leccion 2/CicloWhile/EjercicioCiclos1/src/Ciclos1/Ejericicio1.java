
/*
Ejercicio 1: Lerr un numero y mostrar su cuadrado, repetir
el proceso hasta que se introduzca un numero negativo.
*/
package Ciclos1;

import javax.swing.JOptionPane;




public class Ejericicio1 {
    public static void main(String[] args) {
        
        
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
        
        while(numero >= 0){
            cuadrado = (int)Math.pow(numero,2);
            System.out.println("El numero "+numero + " elevado al cuadrado es "+cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero: "));
        }
        System.out.println("El programa a finalizado por haber ingresado un numero negativo");
    }
}