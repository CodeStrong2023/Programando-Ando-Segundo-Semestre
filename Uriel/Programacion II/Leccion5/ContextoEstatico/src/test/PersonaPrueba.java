package test;

import domain.Persona;

public class PersonaPrueba {
    private int contador;
    public static void main(String[] args) {
        //this.contador = 10; No se puede referenciar desde un contexto estatico
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getContador());
        Persona persona1 = new Persona("Uriel");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("Gaston");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
    }
    
    public static void imprimir(Persona persona){
        System.out.println("persona = " + persona);
    }
    
    public int getContador(){
        imprimir(new Persona("Jesus"));
        return this.contador;
    }
}
