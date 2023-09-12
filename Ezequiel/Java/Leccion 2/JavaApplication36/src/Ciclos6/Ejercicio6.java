
package Ciclos6;

import javax.swing.JOptionPane;

/*
Pedir numeros hasta que se teclee un 0, mostrar la suma de todos los numeros introducidos
 */
public class Ejercicio6 {
    public static void main(String[] args) {
        int numero, suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")); 
            
            suma+= numero; 
        } while(numero != 0);
        JOptionPane.showMessageDialog(null,"La suma de los numeros ingresados es: " + suma);
    }
}
