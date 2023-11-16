
//Ejercicio 3: Leer 5 numeros por teclado, almacenarlos en un arreglo
//y a continuacion realizar la media de los positivos,
//la media de los negativos y contar el numero de ceros

package ejercicios;

import javax.swing.JOptionPane;

public class Ejercicio3 {
     public static void main(String[] args) {
        int numeros[] = new int[5], ceros =0, positivos =0, negativos =0, suma_neg=0, suma_pos=0;
        for (int i = 0; i < 5; i++) {
            numeros[i] = Integer.parseInt(JOptionPane.showInputDialog("Digite el valor en el indice "+i));
        }
        for (int i = 0; i < 5; i++) {
            if (numeros[i]<0) {
               negativos++; 
               suma_neg += numeros[i];
            }
            else if(numeros[i]>0){
                positivos++;
                suma_pos += numeros[i];
            }
            else
                ceros++;
        }
         System.out.println("La suma de ceros es "+ceros);
         System.out.println("La media de los positivos es "+(suma_pos/positivos));
         System.out.println("La media de los negativos es "+(suma_neg/negativos));
    }
}
