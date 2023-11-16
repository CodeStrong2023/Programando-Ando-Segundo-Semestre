package ejercicios;

import javax.swing.JOptionPane;

public class Ejercicio3 {
    public static void main(String[] args) {
        int matriz[][] = new int[3][3];
        System.out.println("Rellenar la matriz");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor de la "+i+"° fila, "+j+"° columna"));
            }
        }
        JOptionPane.showMessageDialog(null, "Matriz normal\n");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                JOptionPane.showMessageDialog(null, "["+matriz[i][j]+"]");
            }
            JOptionPane.showMessageDialog(null, "\n");
        }
        JOptionPane.showMessageDialog(null, "Matriz compuesta\n");
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                JOptionPane.showMessageDialog(null, "["+matriz[j][i]+"]");
            }
            JOptionPane.showMessageDialog(null, "\n");
        }
    }
}
