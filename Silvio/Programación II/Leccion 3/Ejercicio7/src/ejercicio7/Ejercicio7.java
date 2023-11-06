/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio7;

import java.util.Scanner;

/**
 *
 * @author Silvio
 */
public class Ejercicio7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner entrada = new Scanner(System.in);
        final int salario = 1000;
        int comision = 150, venta;
        float salarioMensual, ventaCarro,porcVenta, totalPrecio;
        
        System.out.println("Digite la cantidad de carros vendidos: ");
        venta = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio de un carro: ");
        ventaCarro = Float.parseFloat(entrada.nextLine());
        
        comision *= venta;
        totalPrecio = ventaCarro * venta;
        porcVenta = totalPrecio * 0.05f;
        salarioMensual = salario + comision + porcVenta;
        
        System.out.println("\nEl salario mensual es: "+salarioMensual);
    }
    
}
