package Ciclos05;

import javax.swing.JOptionPane;

public class CiclosJOP05 {
    public static void main(String[] args) {
        int aleatorio, numero, contador= 0;
        aleatorio = (int)(Math.random()*100);
        do{
            System.out.println("Digite un numero");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "El numero ingresado es menor al que busca");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "El numero ingresado es mayor al que busca");            }
            else{
                JOptionPane.showMessageDialog(null, "El numero es igual");
            }
            contador++;
        }while(numero != aleatorio);
        System.out.println("Se realizaron "+contador+" intentos");
    }
}
