/*
Ejercicio11: Diseniar un programa que muestre el producto
de los 10 primeros numeros impares
Hacerlos con JOptionPane
*/
package ciclos11;

import javax.swing.JOptionPane;

public class Ciclos11 {
    public static void main(String[] args) {
        
        long producto = 1;
        for(int i = 1; i <= 20 ; i += 2){//el aumento apujnta a solo ir por numeros impares
                     producto *= i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los numeros impares es: " + producto);
    }
    
}
