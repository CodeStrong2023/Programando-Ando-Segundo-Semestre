/*
ejercicio 7: pedi numeros hasta que se introduzca uno negativo
y calcular la media
*/
package ciclos07;

import javax.swing.JOptionPane;

public class ejercicio07 {
    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while(numero >= 0){ //mientras el numero no sea negativo
            suma  += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
            
        }
        if(conteo==0){
            JOptionPane.showMessageDialog(null, "error, la division entre cero no existe");
        }
        else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null, "el promedio es: "+promedio);
        }
    }
}
