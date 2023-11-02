package leccion2;

import java.util.Scanner;

public class leccion2 {

    public static void main(String[] args) {
//       var condicion = true;
//       if (condicion) {
//           System.out.println("condicion verdadera");//condicional simple
//       }
//       else{
//           System.out.println("condicion falsa");//condicional doble
//       }
//       var numero = 2;
//       var numeroTexto = "numero desconocido";
//       if (numero == 1){
//           numeroTexto = "numero uno";
//       }
//       else if (numero == 2){
//           numeroTexto = "numero dos";
//       }
//       else if (numero == 3){
//           numeroTexto = "numero tres";
//       }
//       else if (numero == 4){
//           numeroTexto = "numero cuatro";
//       }
//       else{
//           numeroTexto = "numero no encontrado";
//       }
//        System.out.println("numeroTexto = " + numeroTexto);
        Scanner entrada = new Scanner(System.in);
        System.out.println("digite un numero del 1 al 4");
        var numero = Integer.parseInt(entrada.nextLine());
        var numeroTexto = "valor desconocido";
        switch (numero) {
            case 1:
                numeroTexto = "numero uno";
                break;
            case 2:
                numeroTexto = "numero dos";
                break;
            case 3:
                numeroTexto = "numero tres";
                break;
            case 4:
                numeroTexto = "numero cuatro";
                break;
            default:
                numeroTexto = "caso no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);
        
        
        
        
    }
}
