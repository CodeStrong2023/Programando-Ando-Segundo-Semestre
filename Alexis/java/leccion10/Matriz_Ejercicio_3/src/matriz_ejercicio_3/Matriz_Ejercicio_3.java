// ejercicio3: crear ycargar un matriz de tamaño 3x3, trasponerla y mostrarla
package matriz_ejercicio_3;

import java.util.Scanner;

public class Matriz_Ejercicio_3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz [][] = new int [3][3];
        System.out.println("rellenar la matriz: ");
        for(int i=0;i<3;i++){
            for (int j = 0; j < 3; j++) {
                System.out.println("matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        System.out.println();
        
        //matriz transpuesta
        System.out.println("matriz original: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.println(matriz[j][i]+" ");
            }
            System.out.println();
        }
        System.out.println();
    }
    
}
