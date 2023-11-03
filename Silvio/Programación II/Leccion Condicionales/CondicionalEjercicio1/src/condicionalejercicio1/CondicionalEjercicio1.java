/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package condicionalejercicio1;

import java.util.Scanner;

/**
 *
 * @author Fraggah
 */
public class CondicionalEjercicio1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un mes del año: ");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "Estacion desconocida";
        if(mes == 1 || mes ==2 || mes == 3){
            estacion = "Verano";
        }
        else if(mes == 4 || mes ==5 || mes == 6){
            estacion = "Otonio";
        }
        else if(mes == 7 || mes ==8 || mes == 9){
            estacion = "Invierno";
        }
        else if(mes == 10 || mes ==11 || mes == 12){
            estacion = "Primavera";
        }
        System.out.println("Estacion = "+ estacion);
    }
    
}
