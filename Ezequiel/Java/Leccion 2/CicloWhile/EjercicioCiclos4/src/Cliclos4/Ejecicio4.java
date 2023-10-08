
package Cliclos4;

import javax.swing.JOptionPane;

/**
 Ejercicio 4
 * Pedir numeros hasta que se teclee uno negattivo y mostrar cuantos numeros se han introducido.
 * primero con la clase scanner y luego JOptionPane
 * 
 */

public class Ejecicio4 {
    public static void main(String[] args) {
        int numero, conteo =0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0){  
           JOptionPane.showMessageDialog(null,"El numero " +numero + " es Positivo");
           conteo++;
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
       }
        JOptionPane.showMessageDialog(null,"Ha ingresado " +conteo + " numeros que no son negativos");
    }
}
