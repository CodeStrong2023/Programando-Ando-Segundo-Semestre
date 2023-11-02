
package ciclos12;

import javax.swing.JOptionPane;

/*
 Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con las dos Clases, Scanner y JOptionPane
 */
public class Ciclos12JOptionPane {
    public static void main(String[] args) {
        long factorial = 1;
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        for(int i = 1; i<= numero; i++){
            factorial *= i;
        }
        JOptionPane.showMessageDialog(null, "\nEl factorial del numero ingresado es: " + factorial);
    }
}
