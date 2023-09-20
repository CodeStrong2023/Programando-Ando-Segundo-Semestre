
package operaciones;

public class aritmetica {
    // atributos de la clase
    int a;
    int b;
    
    //metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        int resultado = this.a + this.b;
        return resultado;
    }
    
    public int sumarConArgumentos(int a, int b){
        this.a = a; //el argumento a se asigna al tributo this.a
        this.b = b;
        //return a + b;
        return sumarConRetorno();
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}
