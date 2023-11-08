/*
Ejercicio 5: Crear y cargar una matriz de tamanio n x m, mostrar la suma de cada fila y cada columna.
*/
package matriz_ejercicio_5;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Matriz_Ejercicio_5 {
     public static void main(String[] args) {
        
         Scanner entrada = new Scanner(System.in);
         int matriz [][], nFilas, nCol, sumaFilas, sumaCol;
         int posFila = 0, posCol = 0;
         
         nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de filas: "));
         nCol = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de columnas: "));
         
         matriz = new int [nFilas][nCol];
         int filas[]= new int [nFilas];
         int columnas[]= new int [nCol];
         
         System.out.println("Rellenado de la Matriz: ");
         for (int i = 0; i < nFilas; i++){
             for (int j = 0; j < nCol; j++){
                 System.out.print("Matriz ["+i+"]["+j+"]: ");
                 matriz[i][j]= entrada.nextInt();
             }
         }
         
         System.out.println("\n Matriz Original: ");
         for(int i = 0; i < nFilas; i ++){
             for (int j = 0; j < nCol; j ++){
                 System.out.print(matriz [i][j]+" ");
             }
             System.out.println("");
         }
         //sumando las filas
         for (int i = 0; i<nFilas; i ++){
             sumaFilas = 0;
             for(int j =0; j<nCol; j++){
                 sumaFilas += matriz[i][j];
             }
             filas[posFila] = sumaFilas;
             posFila ++;
         }
         
         //Sumando las columnas
         for(int j = 0; j<nCol; j++){
             sumaCol = 0;
             for(int i = 0; i< nFilas; i ++){
                 sumaCol += matriz [i][j];
             }
             columnas[posCol]=sumaCol;
             posCol++;
         }
         
         System.out.println("\n La cuma de las filas es: ");
         for(int i = 0; i < nFilas; i ++){
             System.out.print(filas[i]+ " - ");
         }
         System.out.println("");
         
         System.out.println("\n La suma de las Columnas es: ");
         for ( int i = 0; i < nCol; i++){
             System.out.print(columnas[i]+ " - ");
         }
         System.out.println("");
                  
    }
    
    
    
}
