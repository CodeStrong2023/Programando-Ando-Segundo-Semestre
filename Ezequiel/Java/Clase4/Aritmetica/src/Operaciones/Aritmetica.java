
package Operaciones;

public class Aritmetica {
    int a;
    int b;
    
    //Sobrecarga de contructores
    public Aritmetica(){
        System.out.println("Se esta ejecutando el constructor numero uno");
    }
    
    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se esta Ejecutando el constructor numero dos");
    }
    
    
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
