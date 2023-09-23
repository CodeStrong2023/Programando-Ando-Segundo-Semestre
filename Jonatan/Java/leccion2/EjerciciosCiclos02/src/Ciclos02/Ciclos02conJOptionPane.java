
package Ciclos02;

//importamos la extencion 
import javax.swing.JOptionPane;//importamos el JOptionPane

public class Ciclos02conJOptionPane {
    public static void main(String[] args) {
        
        //en la misma declaracion de variable incicializamos el input
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));//reemplazamos el metodo scanner por JOptionPane
        while(numero != 0 ){//ciclo while si es igual a 0 se termina el programa
            if(numero > 0){//si el numero es positivo a 0 se
                System.out.println("El numero "+numero+" es POSITIVO");
            }
            else{
                System.out.println("El numero "+numero+" es NEGATIVO");
                
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        
        System.out.println("El numero "+numero+" finaliza el programa");
    }
}
