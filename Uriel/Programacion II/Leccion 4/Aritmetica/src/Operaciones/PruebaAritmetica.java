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
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 a: "+aritmetica2.a);
        System.out.println("aritmetica2 b: "+aritmetica2.b);
    }
    public static void miMetodo(){
        //a = 10;
        System.out.println("Aqui hay otro metodo");
    }
}
