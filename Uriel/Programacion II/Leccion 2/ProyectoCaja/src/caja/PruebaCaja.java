package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        System.out.println("Calculo con el constructor vacio");
        Caja caja1 = new Caja();
        caja1.altura = 5;
        caja1.ancho = 10;
        caja1.profundidad = 8;
        System.out.println("El volumen de la caja es "+caja1.calcularVolumen()+"cm3");
        System.out.println("\nCalculo con el constructor por parametro");
        Caja caja2 = new Caja(6, 7, 11);
        System.out.println("El volumen de la caja es "+caja2.calcularVolumen());
    }
}
