package Operaciones;

public class PruebaAritmetica {

    public static void main(String[] args) {
        var a = 12;//Variables locales en memoria Stack
        int b = 7;//Variables locales en memoria Stack
        miMetodo();
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        //Para almacenar u objeto o los atributos se usa la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        //Metodos con paso de argumentos
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);

        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 a: " + aritmetica2.a);
        System.out.println("aritmetica2 b: " + aritmetica2.b);
        Persona persona = new Persona("Uriel", "Pardo");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: " + persona.nombre);
        System.out.println("Persona apellido: " + persona.apellido);
    }

    public static void miMetodo() {
        //a = 10;
        System.out.println("Aqui hay otro metodo");
    }
}
//Nueva clase persona con el constructor

class Persona {

    String nombre;
    String apellido;

    Persona(String nombre, String apellido) {//Constructor
        //super();//Llamada al constructor de la clase Padre object
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);
    }
}

class Imprimir{
    public Imprimir() {
        super();
    }

    public void imprimir(Persona persona) {
        System.out.println("Persona desde la clase imprimir: " + persona);
        System.out.println("Impresion del objeto actual(this):" + this);
    }
}
