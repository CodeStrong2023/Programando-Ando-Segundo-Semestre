
package Clases;

public class Persona {
// Atributos de la clase (caracteristicas)
    String nombre;
    String apellido;
    
    //Metodos de la clase (Acciones)
    //un metodo es una aprte de codigo que vamos a poder reutilizar
    //un metodo puede recibir valores estos se conocen como argumentos
    //un metodo tambien puede regresar un valor a esto s elo llama valor de retorno que tambien puede regresar a nuestro metodo
    
    public void obtenerInformacion(){
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellido: "+apellido);
    }
}