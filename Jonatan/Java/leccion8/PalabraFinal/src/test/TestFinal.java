/*
uso de la palabra final
esta palabra tiene diferentes significados dependiendo donde
se aplique:
Variables: evita cambiar el valor que almacena la variable.
metodo:evita que se modifique la definicion o el comportamiento 
        de un metodo desde la subclase(hija)
clases: evita que se creen clases Hijas

Otra caracteristica es que normalmente, cuando trabajamos con variables
se combina con el modificador de acceso estatico para convertir una 
variable en una constatnte, es decir que no se puede modificar su valor,
el ejemplo de esto es una clase MAth en la cual todos sus atributos 
son de tipo static y final, es por eso que la variable pi* se conoce como una
constante
*/
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39999567;
        System.out.println("miDni = " + miDni);
       // miDin = 20312321;//no se puede modificar una variable "FINAL" seria una constante
       // Persona.CONSTANTE_AQUI = 9;//no se modifica
        System.out.println("Mi atributo constante es: " +Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona();//No se puede Asignar una nueva Referencia
        persona1.setNombre("Martin Marilu");
        System.out.println("Persona1 nombre: " +persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("Persona1 nombre: " +persona1.getNombre());
        
    }
}
