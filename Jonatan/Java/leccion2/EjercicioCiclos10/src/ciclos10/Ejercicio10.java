
/*
Ejercico 10 : Pedir 10 numeros y escribir l;a suma total
hacerlo con la clase Scanner y la JOptionPane
*/

package ciclos10;

import javax.swing.JOptionPane;//importamos JOptionPane

public class Ejercicio10 {
    public static void main(String[] args) {
        int numero, suma = 0;//iniciamos variables y contador de suma en 0
        for(int i = 1; i <= 10; i++){//ciclo determinado de movimientos FOR hasta 9
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma += numero;//se acumula la suma en la variable suma
        }
        JOptionPane.showMessageDialog(null,"La suma de todos los numeros es: " + suma);
    }
    
}
