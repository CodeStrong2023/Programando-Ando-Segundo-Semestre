
package ciclos10;

import javax.swing.JOptionPane;

/*
Ejercicio 10: Perdir 10 numeros y escribir la suma total
Hocerlo con la clase Scanner y JOptionPane
 */
public class Ciclos10JOptionPane {
    public static void main(String[] args) {
        int suma = 0;
        for(int i = 1; i <= 10; i++){
            var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null, "\nLa suma de todos los numeros es: "+ suma);
    }
}
