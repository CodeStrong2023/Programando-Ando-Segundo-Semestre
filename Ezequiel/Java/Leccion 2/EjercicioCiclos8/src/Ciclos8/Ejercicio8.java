/*
Ejerciico 8:

pedir un numero N a usuario y mostrar todos los numeros desde
el 1 al N

con clase JOptionPane
*/

package Ciclos8;

import javax.swing.JOptionPane;


public class Ejercicio8 {

    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        int i = 1;
        
        while(i <= numero){
            JOptionPane.showMessageDialog(null, i);
            i++;
        }
    }
}
