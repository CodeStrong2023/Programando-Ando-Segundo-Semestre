package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Zapatillas", 49500.00);
        Producto producto4 = new Producto("Buzo", 19900.00);
        Producto producto5 = new Producto("Celular", 39500.00);
        Producto producto6 = new Producto("Remera", 9900.00);
        Producto producto7 = new Producto("Gorra", 9500.00);
        Producto producto8 = new Producto("Reloj", 39900.00);
        Producto producto9 = new Producto("Calza", 13999.00);
        Producto producto10 = new Producto("Camiseta", 29900.00);
        Producto producto11 = new Producto("Pantalon Jean", 10500.00);
        Producto producto12 = new Producto("Saco", 39999.00);
        
        
        
        
        Orden orden1 = new Orden();
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto12);
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto2);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto9);
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto11);
        orden3.mostrarOrden();
        
        Orden orden4 = new Orden();
        orden4.agregarProducto(producto4);
        orden4.agregarProducto(producto8);
        orden4.agregarProducto(producto6);
        orden4.agregarProducto(producto6);
        orden4.mostrarOrden();
        
        Orden orden5 = new Orden();
        orden5.agregarProducto(producto5);
        orden5.agregarProducto(producto10);
        orden5.agregarProducto(producto1);
        orden5.mostrarOrden();
    }
}
