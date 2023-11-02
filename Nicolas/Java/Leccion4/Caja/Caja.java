/*
 * Proyecto caja:
 * Ejercicio 1: Crear un proyecto segun las especificaciones
 * mostradas a continuacion.
 * La formula es: volumen = ancho * alto * profundidad
 */
public class Caja {
    //Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundo;
    // Metodo y constructores (acciones)
    public Caja() { // Constructor 1 = vacio
    }
    // Constructor con parámetros
    public Caja(int ancho, int alto, int profundo) { // Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;

    }

    public int calcularVolumen() { // Metodo para calcular
        return ancho * alto * profundo;
    }
}