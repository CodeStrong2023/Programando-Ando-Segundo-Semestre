package Ciclos09;

import javax.swing.JOptionPane;

public class CiclosJOP09 {

    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite un dia"));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite un mes"));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite un año"));
        if (1 <= dia && dia <= 30) {
            if (1 <= mes && mes <= 12) {
                JOptionPane.showMessageDialog(null, "La fecha es valida");
                JOptionPane.showMessageDialog(null, dia + "/" + mes + "/" + anio);
            } else {
                JOptionPane.showMessageDialog(null, "El mes es invalido");
            }
        } else {
            JOptionPane.showMessageDialog(null, "El dia es invalido");
        }
    }
}
