
package domain;

public class Persona {

    //cargamos los atributos de la Clase
    private int idPersona;
    private static int contadorPersona;
    private String nombre;
    
    //constructor
    public Persona(String nombre){
        this.nombre = nombre;
        //Incrementar el contador por cada objeto nuevo
        
        Persona.contadorPersona++;//no utilziar el operador this, se  utiliza a travez de la clase
        //vamos a asignar un nuevo valor a la variable idPersona
        this.idPersona = Persona.contadorPersona;
        
    }

    public static int getContadorPersona() {
        return contadorPersona;
    }

    public static void setContadorPersona(int aContadorPersona) {
        contadorPersona = aContadorPersona;
    }
    
    public int getIdPersona() {
        return this.idPersona;
    }

    public void setIdPersona(int idPersona) {
        this.idPersona = idPersona;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
    
}
