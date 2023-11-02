package Ciclos04;

import javax.swing.JOptionPane;

public class CiclosJOP04 {
    public static void main(String[] args) {
        var conteo = 0;
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(numero >= 0){
            System.out.println("El numero "+numero+" es positivo");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        }
        System.out.println("HA ingresado "+conteo+" numeros no negativos");
    }
}
