
package test;

import domain.Persona;

public class PersonaPrueba {
    private int contador;
    
    public static void main(String[] args) {
        Persona persona1 = new Persona("ariel");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("naty");
        imprimir(persona1);
        imprimir(persona2);
        //this.contador = 10; //no se puede referenciar desde un contexto estatico
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getContador());
        
    }
    public static void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    
    public int getContador(){
        imprimir(new Persona("liliana"));
        return this.contador;
    }
}
