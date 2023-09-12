
package Ciclos7;

import javax.swing.JOptionPane;

/**
Pedir numeros hasta que se introduzca un negativo y calcular la media
 */
public class Ejercicio7 {
    public static void main(String[] args) {
        int numero, suma = 0, conteo = 0;
        float promedio = 0;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")); 
        while(numero >= 0){
           suma += numero;
           conteo++;
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: ")); 
        }
        if(conteo == 0){
            JOptionPane.showMessageDialog(null,"Error, la division entre cero no existe");
        }else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null,"El promedio es: " +promedio);
        }
    }
}

