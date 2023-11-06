package domain;

public class Persona {
    //Atributos de herecia
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direcccion;
    
    //Constructor vacio: es para crear objetos sin la necesidad de inicializar
    public Persona(){ //Constructor 1
        
    }
    public Persona(String nombre){//Constructor 2
        this.nombre = nombre;
    }

    public Persona(String nombre, char genero, int edad, String direcccion) {//Constructor 3
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direcccion = direcccion;
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

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getDirecccion() {
        return this.direcccion;
    }

    public void setDirecccion(String direcccion) {
        this.direcccion = direcccion;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona{");
        sb.append("nombre=").append(nombre);
        sb.append(", genero=").append(genero);
        sb.append(", edad=").append(edad);
        sb.append(", direcccion=").append(direcccion);
        sb.append(", ").append(super.toString());

        sb.append('}');
        return sb.toString();
    }

    
    
}
