
package Ciclos5;

import javax.swing.JOptionPane;

/*
 Realizar un juego para adivinar un numero, para ello generar
un numero aleatorio entre el 0 -100, y luego ir pidiendo numeros indicando
"es mayor" o "es menor " segun sea con respecto a N
El poceso termina cuando el usuario acierta y mortramos el numero de intentos
 */
public class Ejercicio5 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100);
        do{
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: ")); 
            
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null,"Digite un numero mayor");
            }
            else if(numero> aleatorio){
                JOptionPane.showMessageDialog(null,"Digite un numero menor");
            }
            else{
                JOptionPane.showMessageDialog(null,"FELICIDADES has adivinado el numero");
            }
            conteo++;
        } while(numero != aleatorio);
        JOptionPane.showMessageDialog(null,"Adivinaste el numero en: " +conteo+ " intentos");
    }
}
