/*
 Ejercicio N7: pedir numeros hasta que se introduzca uno negativo
 y calcular el promedio
 */
package Ciclos07;

import javax.swing.JOptionPane;


public class Ejercicio07 {
    public static void main(String[] args) {
        
        int numero, conteo = 0, suma = 0;//declaramos e iniciamos las variables
        float promedio = 0;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un Numero"));
        while( numero >= 0){//mientras el numero no sea negativo
            suma += numero;//sumamos los numeros que ingresa el usuario
            conteo++;//conteo de los numeros
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro Numero"));
        }
        if(conteo == 0){
            JOptionPane.showMessageDialog(null,"Error, la divicion entre cero no existe");
        }
        else {
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null,"El promedio es: "+promedio);
        }
        
        
        
    }
    
}
