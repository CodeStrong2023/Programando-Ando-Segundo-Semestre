
package test;

import operaciones.Operaciones;

public class TestOperaciones {
    public static void main(String[] args) {
        var resultado = Operaciones.sumar(7,9);
        System.out.println("resultado = " + resultado);
        
        var resultado2 = Operaciones.sumar(7.0,9);
        System.out.println("resultado2 = " + resultado);
        
        var resultado3 = Operaciones.sumar(7,9L);
        System.out.println("resultado3 = " + resultado);
    }
}
