
public class Persona {
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;

    // Constructor vacio: este es para crear objetos sin necesidad de inicializar
    // los atributos de la clase
    public Persona() { // Constructor 2

    }

    public Persona(String nombre) { //Constructor 2
        this.nombre = nombre;

    }

    public Persona(String nombre, char genero, int edad, String direccion) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;

    }

    public String getDireccion () {
        return this.direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;

    }

    public String getNombre() {
        return nombre;

    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return this.genero;
    }

    public void  setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return this.edad;
    }


    @Override
    public String toString() {
        return "Persona{" + "nombre= "+nombre+ ",genero"+genero +", edad" +edad;
    }







    



}