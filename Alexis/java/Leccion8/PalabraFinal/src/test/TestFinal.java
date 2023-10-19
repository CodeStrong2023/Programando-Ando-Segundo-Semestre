/*
uso de la palabra Final
esta palabra tiene diferentes significados dependiendo dende se aplique
    variables: evita cambiar el valor quealmacena la variable
    metodos: evita que se modifique la definicion o el comportaiento
            de un metodo desde una subclase (hija)
    clases: evita que se creen clases hijas
otra caracteristica es que normalmente, cuando trabajamos con variables
se combina con el modificador de acceso estatico para convertir una
variable en una contante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clase Math en la cual todos sus atributos
son de tipo static y final, es por estoque la variable pi* se conoce
como una constante
*/
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39555278;
        System.out.println("miDni = " + miDni);
        //miDni = 20312321; no se puede modificar
        //Persona.CONSTANTE_AQUI = 9;//no se modifica
        System.out.println("mi atributo constantees: "+Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); no se puede asignar una nueva referencia
        persona1.setNombre("ariel betancut");
        System.out.println("persona1 nombre: "+persona1.getNombre());
        persona1.setNombre("liliana");
        System.out.println("persona1 nombre: "+persona1.getNombre());
        
    }
}
