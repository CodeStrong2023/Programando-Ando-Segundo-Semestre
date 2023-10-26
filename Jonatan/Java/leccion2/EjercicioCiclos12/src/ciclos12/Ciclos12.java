/*
Ejercicio12: pedir un numero y calcular sui factorial
HAcerlos con las dos clases, scanner y joptionpane
 */
package ciclos12;

import java.util.Scanner;
import javax.swing.JOptionPane;


public class Ciclos12 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        for (int i = 1; i <= numero; i++){
            factorial *= i;
        }
       // System.out.println("\n El factorial del numero ingresado es: "+ factorial);
        JOptionPane.showMessageDialog(null, "El factorial del numero ingresado es: "+ factorial);
    }
    
}
