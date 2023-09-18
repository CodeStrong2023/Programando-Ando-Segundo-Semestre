
package Operaciones;

public class Aritmetica {
    int a;
    int b;
    
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        a = arg1;
        b = arg2;
        return sumarConRetorno();
    }
    
    public int sumarConArgumentosThis(int a, int b){
        this.a = a;
        this.b = b;
        return sumarConRetorno();
    }
    
    
}
