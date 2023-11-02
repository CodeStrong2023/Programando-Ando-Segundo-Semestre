
package PasoPorValor;

public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 20;//variable local
        System.out.println("valorX = " + valorX);    
        cambioValor(valorX); // solo le enviamos una copia
        System.out.println("valorX = " + valorX);
        
    }
    
    public static void cambioValor(int arg1){//parametros por valor
        System.out.println("arg1 = " + arg1);
        arg1 = 15;
    }
}
