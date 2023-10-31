
package test;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Ezequiel", 57000.0);
        System.out.println("empleado1 = " + empleado1);
        
        Cliente cliente1 = new Cliente(new Date(), true, "Ezequiel",'M', 32, "9 de Julio 1214");
        System.out.println("cliente1 = " + cliente1);
    }
}
