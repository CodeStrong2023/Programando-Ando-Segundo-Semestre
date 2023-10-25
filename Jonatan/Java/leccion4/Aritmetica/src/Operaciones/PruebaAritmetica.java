
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
    }
    
    public static void miMetodo(){//nuevo metodo
        //int a = 10;
        System.out.println("Aqui hay otro metodo");
        
    }
    
    
    
}
