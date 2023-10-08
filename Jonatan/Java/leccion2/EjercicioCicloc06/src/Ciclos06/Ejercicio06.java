
package Ciclos06;

import javax.swing.JOptionPane;//inportamos la funcion JOptionPane


public class Ejercicio06 {
    public static void main(String[] args) {
        int numero, suma = 0;//declaramos las variables
        
        do{//ciclo do While
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero :"));//pedimos los datos al usuario
            suma += numero;            
        }while(numero !=0);
        
        JOptionPane.showMessageDialog(null,"La suma de todos los numeros es: "+suma);
        
        
    }
    
    
}
