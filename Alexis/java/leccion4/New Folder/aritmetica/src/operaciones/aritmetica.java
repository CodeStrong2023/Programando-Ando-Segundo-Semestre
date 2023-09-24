
package operaciones;

public class aritmetica {
    // atributos de la clase
    int a;
    int b;
    
    //el constructor es un metodo especial
    public aritmetica(){
        System.out.println("se esta ejecutando este constructor numero uno");
    }
    //estamos viendo lo que se llama sobrecarga de constructores
    public aritmetica(int a, int b){//constructor 2
        this.a = a;
        this.b = b;
        System.out.println("se esta ejecutando este constructor numero dos");
    }
    
    
    
    
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
