/*
Uso de la palabra final
    Esta palabra tiene distintos significados dependiendo de donde se aplique:
variables: Evita cambiar el valor que almacena dicha variable
metodos: Evita que se modifique la definicion o el comportamiento de un metodo desde una subclase
clases: Evita que se creen hijas
Otra caracterisitica es que normalmente, cuando trabajamos variables
se combina con el modificador de acceso estatico para convertir una variable en una constante, es decir que no se puede modificar su valor, 
el ejemplo de esto es la clase Math en la cual sus atributos
son de tipo static y final, es por esto que la variable pi* se conoce como constante
*/
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 40003049;
        System.out.println("miDni = " + miDni);
        //miDni = 42505230; NO se puede modificar
        //Persona.CONSTANTE_AQUI = 9;
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); No se puede asignar una nueva referencia
        persona1.setNombre("Uriel Pardo");
        System.out.println("persona1 nombre: "+persona1.getNombre());
        
        persona1.setNombre("Gaston");
        System.out.println("persona1 nombre: "+persona1.getNombre());
    }
}
