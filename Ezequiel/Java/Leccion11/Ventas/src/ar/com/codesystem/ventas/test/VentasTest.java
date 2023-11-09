
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.Orden;
import ar.com.codesystem.ventas.Producto;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon",9500.00);
        Producto producto2 = new Producto("Campera",29500.00);
        
        Orden orden1 = new Orden();
        
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo Orden = 2
        
        
        Producto producto3 = new Producto("Zapatos", 7500.00);
        Producto producto4 = new Producto("Blusa", 4500.00);
        Producto producto5 = new Producto("Gorra", 1500.00);
        Producto producto6 = new Producto("Reloj", 12500.00);
        Producto producto7 = new Producto("Calcetines", 1200.00);
        Producto producto8 = new Producto("Bolsa", 3500.00);
        Producto producto9 = new Producto("Cinturón", 2500.00);
        Producto producto10 = new Producto("Jersey", 19800.00);
        Producto producto11 = new Producto("Bufanda", 3200.00);

        
        Orden orden2 = new Orden();
        Orden orden3 = new Orden();

        
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto6);

        orden2.mostrarOrden();
        orden3.mostrarOrden();
    }
}
