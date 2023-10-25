/*
    Ejercicio 2: Leer 5 numeros, guardarlos en un arreglo y 
    mostrarlos en el orden inverso
 */
package ejercicios;

import javax.swing.JOptionPane;

public class Ejercicio2 {
     public static void main(String[] args) {
        String numeros[] = new String[5];
        for (int i = 0; i < 5; i++) {
            numeros[i] = JOptionPane.showInputDialog("Digite el valor en el indice "+i);
        }
        for (int i = 4; i >= 0; i--) {
            System.out.println("numeros["+i+"] = "+numeros[i]);
        }
    }
}
