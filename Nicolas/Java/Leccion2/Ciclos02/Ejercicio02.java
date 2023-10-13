/*
 Ejercicio2 : Leer un numero e indicar si es positivo o negativo
 El proceso se repetira hasta que se introduzca un cero 0
 */

import javax.swing.JOptionPane;

public class Ejercicio02 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0) {
            if(numero > 0) {
                System.out.println("El numero "+numero+" es Positivo");
            }
            else{
                System.out.println("El numero "+numero+" es Negativo");
            }
        
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        System.out.println("El numero "+numero+" finaliza el programa");
    }
 }