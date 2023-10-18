//un programador debe: buscar soluciones, reparar errores y crear proyecytos desde 0
package Operaciones;

public class Aritmetica {//clase siempre comienza con mayusculas
    //Atributos de la clase
    int a;
    int b;
    
    //METODO
    public void sumarNumeros(){//metodos siempre camel case
        //estas variables se destruyen a terminar de ejecutar el programa
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
        
    }
    
    public int sumarConRetorno(){
        int resultado = a + b;
        return resultado;
    }
    public int sumarConArgumentos(int a, int b){//el argumento es la informacion que va a recibir el metodo
        this.a = a;//el argumento se asigna al atributo this.a
        this.b = b;
        //return a + b;
        return sumarConRetorno();//usamos un metodo dentro de otro metodo :)
    }
    //operador this se crea automaticamente y es opcional
    
}
