
package test;

import domain.Peronsa;

/*
Uso de la palabra final
esta palabra tiene diferentes significados dependiendo donde se aplique:
variables: Evita cambiar el valor que almacena la variable
metodos: Evita que se modifique la definicion o el comportamiento de un metodo desde una subclase(hija)
clases evita que se creen clases hijas

otra caracteristica es que normalmente, cuando trabajamos con variables
se ocmbina con el modificador de acceso estatico para convertir una variable
en una constante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clase Math en al clual todos sus atributos son de tipo
static y inal, es por esto que la variable pi* se conoce como una constante.
 */
public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 37831245;
        System.out.println("miDni = " + miDni);
        //miDni = 12345; no me deja por el final

        // Peronsa.CONSTANTE_AQUI = 9; no se modifica
    }
}
