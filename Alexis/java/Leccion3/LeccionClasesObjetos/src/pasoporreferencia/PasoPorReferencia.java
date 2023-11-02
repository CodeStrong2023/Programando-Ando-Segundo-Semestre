//paso por referencia
package pasoporreferencia;

import clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        System.out.println("el cambio que hcimos en el nombre es: "+persona1.nombre);
        persona1 = cambiarElValor(persona1);
        //Persona persona2 = new Persona();
        Persona persona2 = null;
        persona2 = cambiarElValor(persona2);
        //System.out.println("el nuevo valor del objeto es: "+persona2.nombre);
        
        
    }
    public static void cambiarValor(Persona persona){//paso por referencia
        persona.nombre = "Maria";
    }
    public static Persona cambiarElValor(Persona persona){
        if(persona == null){
            System.out.println("valor de persona es invalido");
        }
        else{
            persona.nombre = "Monica";
            return persona;
        }
        
    }
}
