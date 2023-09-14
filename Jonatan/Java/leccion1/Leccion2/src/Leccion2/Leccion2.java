
package Leccion2;

import java.util.Scanner;


public class Leccion2 {
    public static void main(String[] args) {
        /*
        var condicion = true;
        if (condicion){
            System.out.println("Condicion es verdadera");
        }
        else {
            System.out.println("Condicion es Falsa");
        }
        //Ejercicio con estructura if else
        var numero = 4;
        var numeroTexto = "Numero desconocido";
        if (numero == 1){
            numeroTexto = "Numero uno";
        }
        else if (numero == 2 ){
            numeroTexto = "Numero dos";
        }
        else if (numero == 3 ){
            numeroTexto = "Numero tres";
        }
        else if (numero == 4 ){
            numeroTexto = "Numero cuatro";
        }
        else{
            numeroTexto = "Numero no entontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
        */
        
        // Sentencia de control Switch
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numeor del 1 al 4: ");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "Valor desconocido";
        switch (numero){
            case 1:
                numeroTexto = "Numero uno";
                break;//importante el brak para cortar la sentencia switch
            case 2:
                numeroTexto = "Numero dos";
                break;
            case 3:
                numeroTexto = "Numero tres";
                break;
            case 4:
                numeroTexto = "Numero cuatro";
                break;
            default:
                numeroTexto = "caso no encontrado";
                
        }
        System.out.println("numeroTexto = "+ numeroTexto);
        
        
        
        
        
        
        
        
    
    }
}