/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ifelse102;

/**
 *
 * @author Fraggah
 */
public class IfElse102 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        var numero = 2;
        var numeroTexto = "Numero desconocido";
        if(numero == 1){
            numeroTexto = "Numero uno";
        }
        else if(numero ==2){
            numeroTexto = "Numero dos";
        }
        else if(numero ==3){
            numeroTexto = "Numero tres";
        }
        else if(numero ==4){
            numeroTexto = "Numero cuatro";
        }
        else{
            numeroTexto = "Numero no encontrado";
        }
        System.out.println("numeroTexto = "+ numeroTexto);
    }
    
}
