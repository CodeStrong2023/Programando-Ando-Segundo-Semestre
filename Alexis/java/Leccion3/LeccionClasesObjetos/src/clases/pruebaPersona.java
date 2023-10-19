
package clases;

public class pruebaPersona {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona(); //llamamos al constructor
        persona1.nombre = "ariel"; //el valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "betncud";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = "+persona2);
        System.out.println("persona1 = "+persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "osvaldo";
        persona2.apellido = "giordanini";
        persona2.obtenerInformacion();
        
        
        
        
        
        
        
        
    }
}
