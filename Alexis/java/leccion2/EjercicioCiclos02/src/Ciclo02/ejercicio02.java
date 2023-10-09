/*
ejercicio 2: leer un numero e indicar si es positivo o
negativo. el proceso se repetira hasta que se introdusca 
un cero 0
hacer este ejercicio on la clase scanner,
luego hacerlo nuevamente con la clase JoptionPane
 */
package Ciclo02;
import javax.swing.JOptionPane;
public class ejercicio02 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "el numero "+numero+"es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "el numero "+numero+"es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero"));
        }
        JOptionPane.showMessageDialog(null, "el numero "+numero+" finaliza el programa");
    }
}
