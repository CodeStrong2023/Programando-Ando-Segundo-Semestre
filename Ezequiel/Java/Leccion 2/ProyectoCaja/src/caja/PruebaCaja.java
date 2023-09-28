
package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        
        int madidaAncho = 3;
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja();
        caja1.ancho = madidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen();
        
        System.out.println("Resultado del volumen de la caja 1: " + resultado);
        
        Caja caja2 = new Caja(2, 4, 6);
        
        System.out.println("Resultado del volumen de la caja 2: " + caja2.calcularVolumen());
    }
}
