
package domain;

// Crear y cargar una matriz de tamanio 3x3, transponerla y mostrarla

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][] = new int[3][3];
        
        System.out.println("Rellenar la matriz: ");
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.println("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        System.out.println();
        
        System.out.println("matriz Original: ");
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.print(matriz[i][j]+"");
            }
            System.out.println("");
        }
        System.out.println();
    }
}
