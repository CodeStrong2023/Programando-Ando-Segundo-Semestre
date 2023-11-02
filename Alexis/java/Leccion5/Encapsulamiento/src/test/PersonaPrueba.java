
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("osvaldo", 57000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //modificamos a traves de los metodos
        persona1.setNombre("juan ignacio");
        //persona1.nombre = "juan ignacio"; ya no se puede utilizar
        //System.out.println("nombre es: "persona1.nombre); error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado apra el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        //tarea: crear otroobjeto de tipo persona, asignar valores de manera inicial
        //e imprimir, luego modificar sus valores y volver a imprimir
        
        /*
        Persona persona2 = new Persona("maria", 600, true);
        System.out.println("persona2 su nombre es: "+persona2.getNombre());
        persona2.setNombre("carlos");
        System.out.println("persona2 con su nombre modificado: "+persona2.getNombre());
        System.out.println("persona2 el resultado apra el sueldo: "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+persona2.isEliminado());
        */
        
        System.out.println("persona1 = " + persona1);
        
    }
}
