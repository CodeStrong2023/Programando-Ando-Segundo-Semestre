
package pasoporreferencia;


/*
Los parámetros por referencia son una forma de pasar datos a una función o procedimiento 
donde se pasa una referencia o dirección de memoria de la variable original en lugar de copiar su valor. 
Esto permite que cualquier modificación realizada en el parámetro dentro de la función 
afecte directamente a la variable original fuera de la función.

*/
public class PasoPorreferencia {

    public static void main(String[] args) {
        Persona persona1 = new Persona();
        
        persona1.nombre = "Ester";
        System.out.println("persona1 nombre = " + persona1.nombre);
        
    }
    public static void cambiarValor(Persona persona){
        persona.nombre = "Maria";
    }
}
