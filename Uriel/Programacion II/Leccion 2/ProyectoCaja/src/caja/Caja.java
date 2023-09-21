
package caja;

public class Caja {
    float altura;
    float ancho;
    float profundidad;
    public Caja(){
        
    }
    public Caja(float altura, float ancho, float profundidad){
        this.altura = altura;
        this.ancho = ancho;
        this.profundidad = profundidad;
    }
    
    public float calcularVolumen(){
        return  altura*ancho*profundidad;
    }
}
