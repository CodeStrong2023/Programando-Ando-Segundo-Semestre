/*
Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si
la fecha es corecta. Suponiedno que todos los meses son de
30 dias

*/


package Ciclos9;

import java.util.Scanner;

public class Ejercicio9 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el dia: ");
        int dia = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Digite el mes: ");
        int mes = Integer.parseInt(entrada.nextLine());
        
        System.out.println("Digite el anio: ");
        int anio = Integer.parseInt(entrada.nextLine());
        
        if((dia != 0)&&(dia <= 30)){
            if((mes != 0)&&(mes <= 30)){
                if((anio != 0)&&(anio <= 30)){
                    System.out.println("La fecha ingresada es: "+dia+ "/"+mes+ "/"+anio);
                }
                else{
                    System.out.println("Fecha incorecta, anio incorrecto");
                }
            }
            else{
                System.out.println("Fecha incorecta, mes incorrecto");
            }
        }
        else{
            System.out.println("Fecha incorecta, dia incorrecto");
        }
    }
}
