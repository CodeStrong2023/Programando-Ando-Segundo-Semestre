
package dominio;

public class Persona {
    //atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    
    //constructor
    public Persona(String nombre, double sueldo, boolean eliminado){//asignamos variables
        this.nombre = nombre;//con this asignamos el atributo a la variable
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }
    
    //metodos

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    public String toString(){
        return "Persona { nombre: " + this.nombre+
                ", sueldo: "+this.sueldo+
                ", eliminado: "+this.eliminado+"}";
    }
    
}
