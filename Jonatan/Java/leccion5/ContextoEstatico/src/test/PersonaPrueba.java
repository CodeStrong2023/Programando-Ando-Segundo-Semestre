
package test;
import domain.Persona;

public class PersonaPrueba {
    private int contador;
        
    public static void main(String[] args) {
        Persona persona1 = new Persona("Nicolas");
        System.out.println("persona1 = " + persona1);
        
        Persona persona2 = new Persona("Mariano");
        System.out.println("persona2 = " + persona2); 
        //
        imprimir(persona1);
        imprimir(persona2);
        //this.contador = 10;//no se puede referenciar desde un contecto estatico
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getcontador());
    }
    public static void imprimir(Persona persona){//creamos otro metodo para imprimir
        System.out.println("persona = " + persona);
    }
    
    public int getcontador(){
        imprimir(new Persona("Liliana"));
        return this.contador;
    }
    
}
