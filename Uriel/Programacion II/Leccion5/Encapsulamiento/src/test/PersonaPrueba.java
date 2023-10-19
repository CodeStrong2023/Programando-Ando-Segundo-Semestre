package test;

import dominio.Persona;
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Uriel",300000, false);
        persona1.setNombre("Gaston");
        System.out.println("El nombre de persona1 es: "+persona1.getNombre());
        System.out.println("El sueldo de persona1 es: "+persona1.getSueldo());
        System.out.println("El estado de persona1 es: "+persona1.isEliminado());
        ///Tarea: Crear otro objeto tipo Persona, asignar valores, imprimir, modificar y volver a imprimir
        Persona persona2 = new Persona("Jonathan", 250000, false);
        System.out.println("\n"+persona2.getNombre()+" es programador Java Jr, y gana mensualmente "+persona2.getSueldo()+" y su estado es "+persona2.isEliminado());
        persona2.setSueldo(450000);
        System.out.println("\n"+persona2.getNombre()+" fue ascendido programador Java Ssr, y gana mensualmente "+persona2.getSueldo()+" y su estado es "+persona2.isEliminado());
        
        System.out.println("persona1: "+persona1.toString());
        System.out.println("persona1 = " + persona1);

    }
}
