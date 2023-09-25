
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
        
        persona1 = cambiarElValor(persona1);
        //Persona persona2 = null;
        Persona persona2 = new Persona();
        persona2 = cambiarElValor(persona2);
        
    }
    public static void cambiarValor(Persona persona){
        persona.nombre = "Maria";
    }
    
    public static Persona cambiarElValor(Persona persona){
        if(persona == null){
            System.out.println("Valor de persona es invalido: Null");
            return null;
        }else{
            persona.nombre = "Monica";
            return persona; 
        }
    }
}
