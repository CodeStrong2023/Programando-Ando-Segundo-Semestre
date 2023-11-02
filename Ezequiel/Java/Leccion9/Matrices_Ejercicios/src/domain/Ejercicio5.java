
package domain;

import java.util.Scanner;
import javax.swing.JOptionPane;

/*
Ejercicio 5: Crear y cargar una matriz de tamanio n x m, mostrar la suma de cada 
fila y de cada columna
 */
public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas,nCol,sumaFilas,sumaCol;
        int posFila,posCol;
        
        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de filas"));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de columnas"));
        
        matriz = new int [nFilas][nCol];
        int filas[] = new int[nFilas];
        int columnas[] = new int [nCol];
        
        System.out.println("Rellenar la matriz: ");
        for(int i=0;i<nFilas;i++){
            for(int j=0;j<nCol;j++){
                System.out.println("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        
        System.out.println("matriz Original: ");
        for(int i=0;i<nFilas;i++){
            for(int j=0;j<nCol;j++){
                System.out.print(matriz[i][j]+"");
            }
            System.out.println("");
        }
        
        
        //Sumando las filas
        posFila = 0;
        for(int i=0;i<nFilas;i++){
            sumaFilas = 0;
            for(int j=0;j<nCol;j++){
                sumaFilas += matriz[i][j];
            }
            
            filas[posFila] = sumaFilas;
            posFila++;
        }
        
        //Sumando las columnas
        posCol = 0;
        for(int i=0;i<nCol;i++){
            sumaCol = 0;
            for(int j=0;j<nCol;j++){
                sumaCol += matriz[i][j];
            }
            
            columnas[posCol] = sumaCol;
            posCol++;
        }
        
        System.out.println("\nLa suma de las filas es: ");
        for(int i=0;i<nFilas;i++){
            System.out.println(filas[i]+" - ");
        }
        System.out.println("");
    }
}
