/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo de donde 
se aplique:
       variables: Evita cambiar el valor que almacena la variable.
       metodos: Evita que se modifique la definicion de nn metodo desde una
                 sub clase (hija).
       clases: Evita que se creen clases hijas.
Otra caracteristica es que normalmente, cuando trabajamos con variables
se combina con el modificador de acceso estatico para convertir una
variable en una constante, es decir que no se puede modificar su valor,
son de tipo static y final, es por esto que la variable pi* se conoce
como una constante.

*/
package test;

import domain.Persona;
public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 42266398;
        System.out.println("miDni = " + miDni);
        // miDni = 42123456; // No se puede modificar ya que la definimos como tipo final
        //Persona.CONSTANTE_AQUI = 9; /// No se modifica
        System.out.println("Mi atributo constante es: "+Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona1 = new Persona(); // No se puede asignar porque ya esta definida como final arriba
        persona1.setNombre("Nicolas Sini");
        System.out.println("persona1 nombre: "+persona1.getNombre());
        persona1.setNombre("Matias Sini");
        System.out.println("personal nombre: "+persona1.getNombre());
        
  
    }
    
}
