
package caja;//Package

public class Caja {//clase publica caja
    //atributos(Caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //metodos y constructores(acciones)
    
    public Caja(){//constructor 1  = Vacio
    }
    
    //Constructor con Parametros
    public Caja(int ancho, int alto, int profundo){//contructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){//metodo para calcular
        return ancho * alto * profundo;
        
    }
    
}
