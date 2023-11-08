package ejercicios;

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int fila, columna, suma_fila, suma_columna;
        System.out.println("Ingrese la cantidad de filas de la matriz");
        fila = sc.nextInt();
        System.out.println("Ingrese la cantidad de columnas de la matriz");
        columna = sc.nextInt();
        int matriz[][] = new int[fila][columna];

        for (fila = 0; fila < matriz.length; fila++) {
            for (columna = 0; columna < matriz[fila].length; columna++) {
                   System.out.println("Ingrese el valor de la fila "+(fila+1)+", columna "+columna+1);
                   matriz[fila][columna] = sc.nextInt();
            }
        }
        
        for (fila = 0; fila < matriz.length; fila++) {
            suma_columna = 0;
            for (columna = 0; columna < matriz[fila].length; columna++) {
                suma_columna += matriz[fila][columna];
            }
            System.out.println("La suma de la columna "+(fila+1)+" es: "+suma_columna);
        }
        for (columna = 0; columna < matriz.length; columna++) {
            suma_fila = 0;
            for (fila = 0; fila < matriz[columna].length; fila++) {
                suma_fila += matriz[fila][columna];
            }
            System.out.println("La suma de la fila "+(columna+1)+" es: "+suma_fila);
        }
    }
}
