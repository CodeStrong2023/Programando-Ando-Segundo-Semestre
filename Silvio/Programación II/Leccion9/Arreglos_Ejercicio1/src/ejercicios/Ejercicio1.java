
package ejercicios;

import javax.swing.JOptionPane;

public class Ejercicio1 {
    public static void main(String[] args) {
        String numeros[] = new String[5];
        for (int i = 0; i < 5; i++) {
            numeros[i] = JOptionPane.showInputDialog("Digite el valor en el indice "+i);
        }
        for (int i = 0; i < 5; i++) {
            System.out.println("numeros["+i+"] = "+numeros[i]);
        }
    }
}
