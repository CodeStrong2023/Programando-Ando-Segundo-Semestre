/*
  Ejercicio 4: pedir numeros hasta que se teclee uno negativo, 
  y mostrar cuantos numeros se han introducido.
  lo hacemos con la clase Scanner
  luego lo hacemos con la clase JOptionPane
 */
package Ciclos04;

import javax.swing.JOptionPane;

public class Ejercicio04 {
    public static void main(String[] args) {//psvm + tab para inciar el main
        
        int numero, conteo = 0;//declaramos variables numero y el contador como enteros

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));//iniciamos la clase JOptionPane al mismo tiempo ingresamos la entrada a la variable numero.
        
        while(numero >= 0){//ciclo infinito while hasta que el usuario ingrese un numero negativo. Mientras el numero sea mayor o igual a 0.
            JOptionPane.showMessageDialog(null,"El numero: "+numero+" es POSITIVO.");//Mostramos el numero ingresado y le decimos que es positivo
            conteo++;//agregamos 1 numero mas a la variable contador
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));//pedimos al usuario que ingrese otro numero

          
        }
        JOptionPane.showMessageDialog(null,"A ingresado un numero negativo por lo tanto el programa finaliza.");//cuando el numero ingresado sea NEGATIVO el programa finaliza
        JOptionPane.showMessageDialog(null,"A ingresado una cantidad de: "+conteo+" numeros que no son negativos");
        JOptionPane.showMessageDialog(null,"Gracias por participar.");

        
    }
}
