
package test;

import dominio.Persona;//con * importamos todas las clases dentro del paquete
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Jonathan",200.000,false);// asignamos los atributos del objeto Persona
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: " + persona1.getNombre());
        
        
        // modificamos a traves de los metodos
        persona1.setNombre("Walter Chavero");//con set nombre ingresamos datos
        //persona1.nombre = "Juan manuel";//nombre tiene acceso privado en persona//ya no se usa
        //System.out.println("Nombre es: " + persona1.nombre);//error
        System.out.println("persona1 su nombre nuevo es: " + persona1.getNombre());//con get nombre mostramos datos
        System.out.println("persona 1 el resultado para sueldo es: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        // Tarea: crear otro objeto de tipo persona, asignar Valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
        System.out.println("\n");
        System.out.println("                :TAREA:");
        Persona persona2 = new Persona("Federico Cabrera", 300.000, true);
        System.out.println("persona2 su nombre es: " + persona2.getNombre());
        System.out.println("persona2 su sueldo es: " + persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+ persona2.isEliminado());
        System.out.println("");
        
        System.out.println("DATOS MODIFICADOS DE LA PERSONA 2 \n");
        persona2.setNombre("Franco Castro");
        persona2.setSueldo(178.000);
        persona2.setEliminado(false);
        
        System.out.println("LOS NUEVOS DATOS SON :");
        System.out.println("persona2 su nombre es: " + persona2.getNombre());
        System.out.println("persona2 su sueldo es: " + persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+ persona2.isEliminado());
        
        System.out.println("");
        
        System.out.println("persona1 = " + persona1);
        
    }
}
