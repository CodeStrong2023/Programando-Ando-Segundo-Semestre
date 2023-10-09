
package domain;

/*
 */
public class Persona {
    private int idPersona;
    
    //al ser estatic no se va a inicializar cada vez que se cree un objeto.
    private static int contadorPersona;
    private String nombre;
    
    //Constructor
    public Persona(String nombre){
        this.nombre = nombre;
        //Incrementar el contador por cada objeto nuevo
        Persona.contadorPersona ++;
        //Se asigna un nuevo valor a la variable idPersona
        this.idPersona = Persona.contadorPersona;
    }
    
    public static int getContadorPersona(){
        return contadorPersona;
    }

    public static void setContadorPersona(int contadorPersona) {
        Persona.contadorPersona = contadorPersona;
    }
    
    
    public int getIdPersona(){
        return idPersona;
    }
    
    public void setIdPersona(int idPersona){
        this.idPersona = idPersona;
    }
    
    public String getNombre(){
        return this.nombre;
    }
    
    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + ", nombre=" + nombre + '}';
    }
    
}
