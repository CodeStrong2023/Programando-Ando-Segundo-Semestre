package test;

import domain.Persona;

public class TestMatrices {

    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);
        edades[0][0] = 5;
        edades[0][1] = 7;
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 25;
        edades[2][1] = 31;
        System.out.println("edades 0-0= " + edades[0][0]);
        System.out.println("edades 0-1= " + edades[0][1]);
        System.out.println("edades 1-0= " + edades[1][0]);
        System.out.println("edades 1-1= " + edades[1][1]);
        System.out.println("edades 2-0= " + edades[2][0]);
        System.out.println("edades 2-1= " + edades[2][1]);
        System.out.println("Recorremos a matriz con for");

        for (int i = 0; i < edades.length; i++) {
            for (int j = 0; j < edades[i].length; j++) {
                System.out.println("Edades " + i + "-" + j + ": " + edades[i][j]);
            }
        }
        
        //Sintaxis clasica
        //String frutas[][]= new String[3][2];
        //Sintaxis simplificada

        String frutas[][] = {{"limon", "pomelo"},{"ciruela","Kiwi"},{"Banana","Manzana"}};
        imprimir(frutas);
        
        Persona personas[][]= new Persona[3][2];
        //Asignamos valores a la matriz
        personas[0][0] = new Persona("Silvio");
        personas[0][1] = new Persona("Luis");
        personas[1][0] = new Persona("Mario");
        personas[1][1] = new Persona("Andrea");
        personas[2][0] = new Persona("Ria");
        personas[2][1] = new Persona("Aina");
        imprimir(personas);
    }
    
    public static void imprimir(Object matriz[][]){
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.println("Matriz " + i + "-" + j + ": " + matriz[i][j]);
            }
        }
    }
}
