/*
ejercicio 4: pedir numeros hasta que se teclee uno negativo
y mostrar cuantos numeros se han introducido 
lo hacemos primero con la clase Scanner
luego lo hacemos con la clase JOptionPane
 */
package ciclos04;

import javax.swing.JOptionPane;


public class ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "el numero "+numero+" es POSITIVO");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "a ingresado "+conteo+" numero que no son negativos");
        
    }
}
