
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10; //Variable local
        int b = 7; //Memoria stack
        miMetodo(); //Llamamos al nuevo metodo
        Aritmetica aritmetica1 = new Aritmetica();
        
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        //Para almacenar un objeto o los atributos se utiliza la memoria Heap
        
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("Resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);
        
        
        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5,8);
        System.out.println("aritmetica2 a: " + aritmetica2.a);
        System.out.println("aritmetica2 b: " + aritmetica2.b);
        //aritmetica1 = null; Nunca utiliar esto, no se debe hacer
        //System.gc(); Metodo para limpiar residuos, es pesado, no usar
        
        Persona persona = new Persona("Ezequiel", "Lorenz");
        System.out.println("Persona: " + persona);
        System.out.println("Persona nombre: " + persona.nombre);
        System.out.println("Persona apellido: " + persona.apellido);
    }
    public static void miMetodo(){
        //a = 10; esta variable esta limitada
        System.out.println("Usando otro metodo");
    }
    
    //Una variable local trabaja con la memoria Stack y la memoria con lo que
    // trabajaan los objetos y atributos es la memoria Heap
}

class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){
        super(); //Llamada al constructor de la clase Padre object
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);
    }
}

class Imprimir{
    public Imprimir(){
        super(); //El constructor de la clase padre, para reservar memoria 
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+ persona);
        System.out.println("Impresion del objeto actual (this): "+ this);
    }
}
