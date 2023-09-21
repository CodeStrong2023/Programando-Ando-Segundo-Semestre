package PasoPorReferencia;

import Clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Ester";
        System.out.println("persona1 = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("El cambio que hicimos en el nombre es "+persona1.nombre);
        persona1 = cambiarElValor(persona1);
        System.out.println("El valor es "+persona1.nombre);
        Persona persona2 = null;
        persona2 = cambiarElValor(persona2);
    }
    
    public static void cambiarValor(Persona persona){//Parametro por referencia
        persona.nombre = "Maria";
    }
    
    public static Persona cambiarElValor(Persona persona){
        if(persona == null){
            System.out.println("Valor de persona es invalido: Null");
            return null;
        }
        else{
            persona.nombre = "Monica";
            return persona;
        }
    }
}
