
package domain;


public class Empleado extends Persona{//con extends indicamos que es hijo de la clase "Persona"
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleados;//para incrementar
    
    //Constructores

    public Empleado(String nombre, double sueldo) {
        super(nombre);
        this.idEmpleado = ++Empleado.contadorEmpleados;//
        this.sueldo = sueldo;
    }

    public int getIdEmpleado() {
        return this.idEmpleado;
    }

    public double getSueldo() {
        return this.sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override//toString
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
    
    
    
}
