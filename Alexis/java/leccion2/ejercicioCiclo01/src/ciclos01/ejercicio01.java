//ejercicio 1: leer un numero y mostrar su cuadrado, repetir
//el proceso hasta que se introduzca un numero negativo
package ciclos01;

import javax.swing.JOptionPane;

public class ejercicio01 {
    public static void main(String[] args) {
       int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while(numero >= 0){//mientras el numero sea igual a 0 o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("el numero "+numero+" elevado al cuadrado es: "+cuadrado);
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
        }
        System.out.println("el programa finalizo por numero negativo"); 
    }
}
