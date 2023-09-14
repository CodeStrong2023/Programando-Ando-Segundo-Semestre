
/*Ejercicio3: Leer numeros hasta que se introduzca un cero
Para cada uno indicar si es par o impar,
primero lo haremos con la clase Scanner 
Luego con la clase JOptionPane
*/

package Ciclos03;

import javax.swing.JOptionPane;//

public class Ejercicio03 {
    public static void main(String[] args) {
        int numero;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));//al poner Integer.parseINT(JOptionPane.) ya nos deberia dejar importar la clase
        
        while(numero != 0){ //ciclo infinito while hasta que el usuario decida terminar poniendo un 0
            if(numero % 2 == 0){//ciclo if para saber si el numero ingresado dividido 2 es igual a 0 
                JOptionPane.showMessageDialog(null,"El numero "+numero+" es PAR");//mostramos al usuario su numero ingresado y que es PAR
            }
            else{//si el numero dividido 2 no es igual a 0 
                JOptionPane.showMessageDialog(null,"El numero "+numero+" es IMPAR");//mostramos al cliente el numero ingresado y le decimos que es IMPAR
            }
            JOptionPane.showMessageDialog(null,"Digite otro numero: ");//pedimos al usuario que ingrese otro numero
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
            
        }//si el usuario ingresa 0 finaliza el programa.
        JOptionPane.showMessageDialog(null,"El numero ingresado es: "+numero+" por lo tanto el programa a finalizado.");                    
    }
    
}
