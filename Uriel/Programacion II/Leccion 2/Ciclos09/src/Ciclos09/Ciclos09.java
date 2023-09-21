package Ciclos09;

import java.util.Scanner;

public class Ciclos09 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite un dia");
        int dia = Integer.parseInt(sc.nextLine());
        System.out.println("Digite un mes");
        int mes = Integer.parseInt(sc.nextLine());
        System.out.println("Digite un anio");
        int anio = Integer.parseInt(sc.nextLine());
        if(1 <= dia && dia<= 30){
            if(1<= mes && mes<=12){
                System.out.println("Es una fecha valida");
                System.out.println(dia+"/"+mes+"/"+anio);
            }
            else{
                System.out.println("Es un mes invalido");
            }
        }
        else{
            System.out.println("Es un dia invalido");
        }
        
    }
}
