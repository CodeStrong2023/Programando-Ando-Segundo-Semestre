/*
Ejercicio 3: Leer numeros hasta que se introduzca un 0.
Para cada uno indicar si es par o impar.
Primero lo hacemos con la clase Scanner
Luego con la clase JOptionPane
*/
package Ciclos03;

import java.util.Scanner;

public class Ciclos03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero");
        int numero = Integer.parseInt(sc.nextLine());
        while (numero != 0) {            
            if(numero % 2 == 0){
                System.out.println("El numero "+numero+" es par");
            }
            else{
                System.out.println("El numero "+numero+" es impar");
            }
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(sc.nextLine());
        }
        System.out.println("El numero ingresado "+numero+" finaliza el programa");
    }
}
