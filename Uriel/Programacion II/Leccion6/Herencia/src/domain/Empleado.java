package domain;

/**
 *
 * @author USR
 */
public class Empleado extends Persona{
    private int idEmpleado;
    private double sueldo;
    private static int contadorEmpleado; //Es para incrementar

    public Empleado(){
        this.idEmpleado = ++Empleado.contadorEmpleado;

    }
    public Empleado(String nombre, double sueldo) {
        //super(nombre); Llamado a traves del padre
        this();
        this.nombre = nombre;//Lo hereda y se puede usar a traves de la herencia
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

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Empleado{");
        sb.append("idEmpleado=").append(idEmpleado);
        sb.append(", sueldo=").append(sueldo);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
    
}
