package ciclos10;

import javax.swing.JOptionPane;

public class CiclosJOP10 {

    public static void main(String[] args) {
        int numero, suma = 0;
        for (int i = 1; i <= 10; i++) {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null, "El valor de la suma es "+suma);
    }

}
