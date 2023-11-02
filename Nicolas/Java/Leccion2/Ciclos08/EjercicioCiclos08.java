/* 
 * Ejercicio 8: Pedir un numero N, y mostrar todos los numeros
 */

import javax.swing.JOptionPane;

public class EjercicioCiclos08 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog(null, "Digite un numero: "));
        int i = 1;
        while( i <= numero) {
            JOptionPane.showMessageDialog(null, i);
            i++;

        }
    }

    
}
