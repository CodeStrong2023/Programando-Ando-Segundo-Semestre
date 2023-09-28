package Clases;

public class PruebaPersona {

    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "Uriel";
        persona1.apellido = "Pardo";
        persona1.obtenerInformacion();
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        persona2.obtenerInformacion();
        persona2.nombre = "Ignacio";
        persona2.apellido = "Pardo";
        persona2.obtenerInformacion();
    }
}
