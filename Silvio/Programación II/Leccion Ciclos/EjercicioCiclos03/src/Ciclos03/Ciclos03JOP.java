package Ciclos03;

import javax.swing.JOptionPane;

public class Ciclos03JOP {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El numero "+numero+" es par");
            }
            else{
                System.out.println("El numero "+numero+" es impar");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        System.out.println("El numero "+numero+" finaliza el programa");
    }
}
