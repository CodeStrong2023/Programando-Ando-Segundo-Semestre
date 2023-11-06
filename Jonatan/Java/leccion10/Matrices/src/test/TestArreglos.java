
package test;

public class TestArreglos {
    public static void main(String[] args) {//lado derecho instanciamos un objeto de tipo objet
        int edades [] = new int [3];//lado izquierdo declaramos la Variable
        System.out.println("edades = " + edades);
        
        edades [0]= 17;
        System.out.println("edades = " + edades[0]);
        edades [1] = 12;
        System.out.println("edades = " + edades[1]);
        edades [2] = 22;
        System.out.println("edades = " + edades[2]);
        
        //edades[3] = 7; //fuera de rango, error en tiempo de ejecucion
        
        for (int i = 0; i < edades.length; i ++){
            System.out.println("Edades y sus elementos " + i + ": " + edades[i]);
        }
    }
    
}
