package test;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Uriel", 57000);
        System.out.println("empleado1 = " + empleado1);
        
        Date date1 = new Date();
        Cliente cliente1 = new Cliente(date1, true, "Gaston", 'M', 27, "9 de Julio 1413");
        System.out.println("cliente1 = " + cliente1);
    
    }
}
