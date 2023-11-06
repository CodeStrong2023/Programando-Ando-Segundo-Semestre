
package test;

import domain.Persona;

public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];//declaramos la matriz y luego instanciamos con new int y asignamos la cantidad de filas y columas
        System.out.println("edades = " + edades);
        
        edades [0][0]=5;//llenado manual por codigo duro
        edades [0][1]=7;//diferente columna
        edades [1][0]=8;
        edades [1][1]=4;
        edades [2][0]=9;//tarea agregar fila que falta
        edades [2][1]=1;
        
        System.out.println("edades 0-0 = "+ edades[0][0]);
        System.out.println("edades 0-1 = "+ edades[0][1]);
        System.out.println("edades 1-0 = "+ edades[1][0]);
        System.out.println("edades 1-1 = "+ edades[1][1]);
        System.out.println("edades 2-0 = "+ edades[2][0]);
        System.out.println("edades 2-1 = "+ edades[2][1]);
        
        //imprimimos la matriz en forma de tabla
        System.out.println("Recoorremos la matriz a travez de un ciclo for");
        
        for(int fila = 0; fila < edades.length; fila ++){
            for(int col = 0; col < edades[fila].length; col++){
                System.out.println("Edades "+fila+ "="+col+": "+edades[fila][col]);
            }
        }
        
        //sintaxis clasica
        //String frutas[][]=new String [3][2];
        
        //sintaxis simplificada
        String frutas [][]= {{"Limon","Pomelo"},{"Ciruela","Kiwi"},{"Banana","Manzana"}};
        imprimir(frutas);
//        for(int i = 0; i < frutas.length; i ++){
//            for(int j = 0; j < frutas[i].length; j++){
//                System.out.println("frutas "+i+ "="+j+": "+frutas[i][j]);
//            }
//        }
        //Creamos una matriz de objetos
        Persona personas[][] = new Persona [2][3];
        //Asignamos valores  ala matriz
        personas[0][0] = new Persona("Ariel");
        personas[0][1] = new Persona("Osvaldo");
        personas[0][2] = new Persona("Monica");
        personas[1][0] = new Persona("Antonia");
        personas[1][1] = new Persona("Canuto");
        personas[1][2] = new Persona("Romina");
        System.out.println("");
        System.out.println("MAtriz de personas");
        System.out.println("");
        imprimir(personas);
             
    }
    
    public static void imprimir(Object matriz[][]){
        for(int i = 0;i < matriz.length; i++){
            for(int j =0; j < matriz[i].length; j++){
                System.out.println("Matriz "+i+ "= "+j+": " +matriz[i][j]);
            }
        }    
    }
    
}
