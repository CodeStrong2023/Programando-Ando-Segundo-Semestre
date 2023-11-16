
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        //agregando mas objetos de tipo productos
        Producto producto3 = new Producto("Remera", 6000.00);
        Producto producto4 = new Producto("Gorra", 3000.00);
        Producto producto5 = new Producto("Remera Mangas Larg", 3500.00);
        Producto producto6 = new Producto("Musculosa", 4000.00);
        Producto producto7 = new Producto("Vestido", 7000.00);
        Producto producto8 = new Producto("Mameluco", 14000.00);
        Producto producto9 = new Producto("Short de Banio", 4000.00);
        Producto producto10 = new Producto("Reloj", 20000.00);
        
        
        Orden orden1 = new Orden();
        Orden orden2 = new Orden();
        Orden orden3 = new Orden();
        
        
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        
        
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        orden3.mostrarOrden();
        
        
        
        
        
    }
    
}
