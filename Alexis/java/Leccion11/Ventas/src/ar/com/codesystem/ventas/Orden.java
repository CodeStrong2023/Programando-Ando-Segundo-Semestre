package ar.com.codesystem.ventas;

public class Orden {
    private int idOrden;
    private Producto productos[];//Declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;
    
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }
    
    public void agregarProducto(Producto producto){
        if(this.contadorProductos <Orden.MAX_PRODUCTOS){
            this.productos[this.contadorProductos++] = producto;
            }
        else{
            System.out.println("Se ha superado el maxido de productos: "+Orden.MAX_PRODUCTOS);
        }
    }
    
    public double calcularTotal(){
        double total = 0;
        for (int i = 0; i < this.contadorProductos; i++) {
            //Producto producto = this.productos[i];
            //total += producto.getPrecio();
            total += this.productos[i].getPrecio();//Manera simplificada
        }
        return total;
    }
    
    public void mostrarOrden(){
        System.out.println("\nId Orden: "+idOrden);
        double totalOrden = this.calcularTotal();
        System.out.println("Total de la orden es: $"+totalOrden);
        System.out.println("Productos de la orden");
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println(this.productos[i]);
        }
    }
}
