
package test;


public class TestMatrices {
    public static void main(String[] args) {
        int edades [][] = new int [3][2];
        System.out.println("edades = " + edades);
        edades[0][0] = 5;
        edades[0][1] = 7;
        edades[1][0] = 8;
        edades[1][1] = 4;
        
        System.out.println("edades 0-0 = " + edades[0][0]);
        System.out.println("edades 0-1 = " + edades[0][1]);
        System.out.println("edades 1-0 = " + edades[1][0]);
        System.out.println("edades 1-1 = " + edades[1][1]);
        System.out.println("Recorremos la matriz a traves del ciclo for");
        
        for(int fila = 0; fila <edades.length;fila++){
            for(int col = 0; col <edades[fila].length;col++){
                System.out.println("edades "+fila+ "-" +col+": "+edades[fila][col]);
            }
        }
        
        //Sintaxis simplificada
        String frutas[][] = {{"Limon", "Pomelo"}, {"Ciruela", "Kiwi"}, {"Banana", "Manzana"}};
        
        for(int i = 0; i <frutas.length;i++){
            for(int j = 0; j <frutas[i].length;j++){
                System.out.println("frutas "+i+ "-" +j+": "+frutas[i][j]);
            }
        }
    }
}
