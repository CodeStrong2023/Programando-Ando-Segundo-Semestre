
package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        int a = 10;//Variables Locales
        int b = 7;//memorioa stack
        miMetodo();//llamamos al metodo nuevo
        Aritmetica aritmetica1 = new Aritmetica();//constructor
        //agregamos valores a los atributos
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        //para almacenar un objeto o los atributos se utiliza memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando Argumentos: " + resultado);
        
        System.out.println("aritmetica1 a: "+ aritmetica1.a);
        System.out.println("aritmetica1 a: "+ aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritmetica1 = null;//mala practica pra liberar memoria
        //System.gc(); es un recolector de basura autentico(Es innsesario ya que al terminar de ejecutar se limpia la memoria autimaticamente)
        Persona persona = new Persona("Ariel","Bentancud");//creamos nuevo obj String
        System.out.println("persona = " + persona);
        System.out.println("Persona nombnre: " + persona.nombre);
        System.out.println("Persona apellido: " + persona.apellido);
    }
    
    //MODULARIDAD CREAMOS UN NUEVO METODO
    public static void miMetodo(){//nuevo metodo
        //int a = 10;
        System.out.println("Aqui hay otro metodo");
        
    }  
}
    //CREAMOS UNA NUEVA CLASE
    //a esta clase solo se puede acceder si estamos en el mismo paquete
class Persona{// al crear 23 clases en la misma plantilla no pueden haber 2 clases PUBLICAS
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){//Constructor
        super();//LLamada  aconstrucro de la clase Padre objet
        //Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.apellido = apellido;
        this.nombre = nombre;
        System.out.println("Objeto persona usando this: "+this);
    }
}
class Imprimir{//constructor
    public Imprimir(){//en constructor de la clase padre, para reservar memoria
        super();
    }
    public void imprimir(Persona persona){//metodo
        System.out.println("Persona desde la clase Imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+this);
    }
}