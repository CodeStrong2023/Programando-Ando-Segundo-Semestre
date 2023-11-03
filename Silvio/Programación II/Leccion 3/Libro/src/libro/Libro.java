
package libro;

import java.util.Scanner;

/**
 *
 * @author Silvio
 */
public class Libro {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
    
    Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su Nombre: ");
        var usuario = entrada.nextLine();
        System.out.println("Usuario = "+usuario);
        System.out.println("Escriba el Titulo: ");
        var titulo = entrada.nextLine();
        System.out.println("Resultado: "+titulo+" "+usuario);
        
    }
    
}
