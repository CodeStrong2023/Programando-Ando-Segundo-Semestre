package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a, b;
    //El constructor es un metodo especial
    public Aritmetica(){
        System.out.println("Se esta ejecutando este constructor numero 1");
    }
    public Aritmetica(int a, int b){
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor numero 2");
    }
    //Metodos
    public void sumarNumeros(){
        int resultado = a+b;
        System.out.println("resultado = " + resultado);
    }
    public int sumarConRetorno(){
        //int resultado = a+b;
        return a+b;
    }
    public int sumarConArgumentos(int a, int b){
        this.a = a;
        this.b= b;
        //return a+b;
        return sumarConRetorno();
    }
}
