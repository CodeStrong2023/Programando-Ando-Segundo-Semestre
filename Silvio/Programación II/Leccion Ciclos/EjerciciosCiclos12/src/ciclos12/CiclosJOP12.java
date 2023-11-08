
package ciclos12;

import javax.swing.JOptionPane;

public class CiclosJOP12 {
    public static void main(String[] args) {
        int factorial = 1;
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite el umero a calcular el factorial"));
        for (int i = 1; i <= numero; i++){
            factorial *= i;
        }
        JOptionPane.showMessageDialog(null, numero+"!= "+factorial);
    }
}
