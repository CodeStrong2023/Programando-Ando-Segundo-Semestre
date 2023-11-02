
package test;

import dominio.Persona;

public class PersonaPrueba {

    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        
        //Modificacion a traves de los metodos
        persona1.setNombre("Ezequiel");
        //persona1.nombre = "Juan" ya no se puede usar, ahora hay q acceder 
        //a traves de los metodos
        
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        System.out.println("persona1 sueldo: " + persona1.getSueldo());
        System.out.println("persona1 bool: " + persona1.getEliminado());
        
        
        //Tarea: crear otro objeto de tipo persona, asignar valores de manera inicial
        // e imprimir, luego modificar sus valores yt volver a imprimir
        
        Persona persona2 = new Persona("Jose", 100.000, true);
        
        persona2.setNombre("Marcos");
        System.out.println("persona1 con su nombre modificado: " + persona2.getNombre());
        System.out.println("persona1 sueldo: " + persona2.getSueldo());
        System.out.println("persona1 bool: " + persona2.getEliminado());
        
        
        System.out.println("persona1: " + persona1.toString());
    }
}
