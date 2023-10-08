
package Ciclos5;

import java.util.Scanner;

/*
 Realizar un juego para adivinar un numero, para ello generar
un numero aleatorio entre el 0 -100, y luego ir pidiendo numeros indicando
"es mayor" o "es menor " segun sea con respecto a N
El poceso termina cuando el usuario acierta y mortramos el numero de intentos
 */
public class Ciclos5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100);
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());  
            
            if(numero < aleatorio){
                System.out.println("Digite un numero mayor");
            }
            else if(numero> aleatorio){
                System.out.println("Digite un numero menor");
            }
            else{
                System.out.println("FELICIDADES has adivinado el numero");
            }
            conteo++;
        } while(numero != aleatorio);
        System.out.println("Adivinaste el numero en: " +conteo+ " intentos");
    }
}
