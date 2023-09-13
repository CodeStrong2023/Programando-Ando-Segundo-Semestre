
package Ciclos2;

import javax.swing.JOptionPane;

/*Leer un numero e indicar si es positivo o negativo
Se corta si ingreso un 0

con JOptionPane
 */


public class Ciclos2OptionPane {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        
        while(numero != 0){
            if(numero> 0){
                JOptionPane.showMessageDialog(null, "El numero " +numero+ " es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "El numero " +numero+ " es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero " +numero+ " finaliza el programa");
    }
}
