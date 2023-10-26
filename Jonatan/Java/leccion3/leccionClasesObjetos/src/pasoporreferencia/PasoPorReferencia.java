//PASO POR REFERENCIA
package pasoporreferencia;

import Clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();//todas las clases genrean clases Objet
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es: "+ persona1.nombre);
        persona1 = cambiarElValor(persona1);
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        System.out.println("El nuevo valor del objeto es: "+persona1.nombre);
    }
    
    public static void cambiarValor(Persona persona){//paso por referencia
        persona.nombre = "Maria";
    
    }
    public static Persona cambiarElValor(Persona persona){//metodo cambiarElValor
        if (persona == null){
            System.out.println("Valor de persona es Invalido : Null");
            return null;
        }
        else{
            persona.nombre = "Monica";
            return persona;//nunca el retyurn se pone al comienzo
        }

        
    }
}
