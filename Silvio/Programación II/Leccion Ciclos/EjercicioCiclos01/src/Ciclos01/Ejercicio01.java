
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
         int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero!"));
        while(numero>=0){
            cuadrado = (int)Math.pow(numero, 2);
            JOptionPane.showConfirmDialog(null, "El cuadrado del numero "+numero+" es "+cuadrado,"Resultado", JOptionPane.DEFAULT_OPTION);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero!"));
        }
        System.out.println("El programa a finalizado por numero negativo") ;
    }
}

