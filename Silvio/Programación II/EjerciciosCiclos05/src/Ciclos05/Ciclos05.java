/*
Ejercicio 5: Realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre 0-100, y luego
ir pidiendo numeros indicando "es mayor" o "es menor" segun corresponda.
El programa termina cuando ingresa el numero correcto, indicar cuantos intentos se hicieron
*/
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int aleatorio, numero, contador= 0;
        aleatorio = (int)(Math.random()*100);
        do{
            System.out.println("Digite un numero");
            numero = Integer.parseInt(sc.nextLine());
            if(numero < aleatorio){
                System.out.println("El numero ingresado es menor al que busca");
            }
            else if(numero > aleatorio){
                System.out.println("El numero ingresado es mayor al que busca");
            }
            else{
                System.out.println("El numero es igual");
            }
            contador++;
        }while(numero != aleatorio);
        System.out.println("Se realizaron "+contador+" intentos");
    }
}
