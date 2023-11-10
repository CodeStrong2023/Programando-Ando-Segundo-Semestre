
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        //agregando mas objetos de tipo productos
        Producto producto3 = new Producto("Remera", 6000.00);
        Producto producto4 = new Producto("Gorra", 3000.00);
        Producto producto5 = new Producto("Zapatillas", 40000.00);
        
        
        Orden orden1 = new Orden();
        
        
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto5);
        
        
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        
        
        
    }
    
}
