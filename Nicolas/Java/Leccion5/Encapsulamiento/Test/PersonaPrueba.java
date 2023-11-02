public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        System.out.println("persona1: "+persona1.toString());


        // Moificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; // Ya no se pude utilizar
        //System.out.println("Nombre es: "+persona1.nombre); // Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resulado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());

        //Tarea. Crear otro objeto de tipo Persona, asignar valores de manera inicial
        // e imprimir, luego modificar sus valores y volver a imprimir


        Persona persona2 = new Persona("Nicolas", 150.000, true);
        System.out.println("persona2 su nombre es: "+persona2.getNombre());

        persona2.setNombre("Nicolas Exequiel Sini");
        System.out.println("persona2 con su nombre modificado: "+persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo. "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+persona2.isEliminado());

        System.out.println("persona1: "+persona1.toString());


    }
}