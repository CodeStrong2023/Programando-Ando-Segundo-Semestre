/*
 Ejercicio 5: Realizar un juego para adivinar un numero, 
para ello generar un numero aleatorio entre 0 - 100, y
luego ir pidiendo numeros indicando "es mayor" o 
"es menor" segun sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos
el numero de intentos hechos.
 */
package Ciclos05;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
                Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;//declaramos las variables
        
        //como generar numero aleatorio
        aleatorio = (int)(Math.random()*100);//convertimos a entero por que la funcion random es de tipo DOUBLE y "*100" es la cantidad de numeros que recorre la aleatoriedad.
        
        do{//ciclo do while
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un Numero: "));//pedimos un numero al usuario
            if(numero < aleatorio){//si el numero ingresado es mayor al numero aleatorio se lo informamos
                JOptionPane.showMessageDialog(null,"Digite un numero MAYOR.");
            }
            else if(numero > aleatorio){//si el numero ingresado es menor al numero aleatorio se lo informamos
                JOptionPane.showMessageDialog(null,"Digite un numero MENOR.");
            }
            else{
                JOptionPane.showMessageDialog(null,"Felicidades. Has adivinado el numero.");//cuando el numero ingresado no es ni mayor ni menor mostramos al usuario un cartel de felicidades        
            }
            conteo++;
        }while(aleatorio != numero);
        JOptionPane.showMessageDialog(null,"Adivinaste el numero en: "+conteo+" intentos");// mostramos la cantidad de intentos realizados.        
    }
    
}
