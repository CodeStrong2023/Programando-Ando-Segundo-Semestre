/*
Ejercicio 4: Pedir numeros hasta que se ingrese un numero negativo.
Indicar cuantos numeros se han ingresado
Hacer primero con Scanner y luego JOptionPane
*/
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite un numero");
        var numero = Integer.parseInt(sc.nextLine());
        var conteo =0;
        while(numero >= 0){
            System.out.println("El numero "+numero+" es positivo");
            conteo++;
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(sc.nextLine());
        }
        System.out.println("Se ingresaron "+conteo+" numeros no negativos");
    }
}
