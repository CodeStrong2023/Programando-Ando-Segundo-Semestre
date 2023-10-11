/*
ejercicio 6: pedir numeros hasta que se teclee un 0, mostrar
la suma de todos los numeros introducidos
*/
package ciclos06;

import javax.swing.JOptionPane;


public class ejercicio06 {
       public static void main(String[] args) {
        int numero,suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
            suma+= numero;
        }while(numero != 0);
        JOptionPane.showMessageDialog(null, "La suma de todos los numeros ingresados es: "+suma);
    }
}
