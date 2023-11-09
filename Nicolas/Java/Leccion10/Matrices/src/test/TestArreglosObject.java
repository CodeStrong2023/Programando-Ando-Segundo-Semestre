
package test;

import domain.Persona;


public class TestArreglosObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Nicolas Sini");
        System.out.println("persona 1 = "+personas[0]);
        
        personas[1] = new Persona("Matias Sini");
        System.out.println("persona 2 = "+personas[1]);
       
        for(int i = 0; i < personas.length; i++) {
            System.out.println("persona "+i+" = "+personas[i]);
        }
        //definir los indices en una sola linea
        String frutas[] = {"Banana", "Pera", "Durazno"};
        for(int i = 0; i < frutas.length ; i++) {
            System.out.println("fruta "+i+" = " + frutas[i]);
        }
        
        
               
    }
    
}
