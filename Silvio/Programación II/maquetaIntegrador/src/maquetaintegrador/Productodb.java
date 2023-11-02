/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package maquetaintegrador;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;
//importar producto clase?

/**
 *
 * @author Silvio
 */
public class Productodb {
    
    ArrayList<Producto> productos;
    public Productodb(){
        
    }  
    
    public void crearArrayList(){
        productos = new ArrayList();
    }
    
    public void insertarAlumno(Producto producto){
        productos.add(producto);
    }  

    public String devolverInformacion(){

        String reporte= "";
        for(int contador=0;contador<productos.size();contador++){

            reporte+=productos.get(contador).getNombre()+
                    " "+productos.get(contador).getCantidad()+
                    " "+productos.get(contador).getPrecio_compra()+
                    " "+productos.get(contador).getPrecio_venta()+"\n";
        }
        return reporte;
    }

    public boolean eliminarProducto(String id){
        boolean encontrado=false;
        for(int contador=0;contador<productos.size();contador++){
            if(productos.get(contador).getId().equals(id)){
                encontrado=true;
                productos.remove(contador);
            }
        }
    return encontrado;
    }

    public void guardarArchivo() throws IOException {
        FileWriter fw = new FileWriter("listaProductos.txt", false);
            File archivo = new File("listaProductos.txt");
            FileWriter escribir;
            try {
                escribir = new FileWriter(archivo, false);
                PrintWriter linea = new PrintWriter(escribir);
                for (Producto a : productos) {
                    linea.println(a.getId() + "," +
                                a.getNombre() + "," +
                                a.getCantidad() + "," +
                                a.getPrecio_compra() + "," +
                                a.getPrecio_venta());
                }
                linea.close();
                escribir.close();
            } catch (Exception e) {
                System.out.println("Error al escribir el archivo");
        }
    }
    public void abrirArchivo() {
        File archivo = new File("listaAlumnos.txt");
        ArrayList<Producto> nuevaLista = new ArrayList<Producto>();
        try (Scanner lector = new Scanner(archivo)) {
            while (lector.hasNextLine()) {
                String linea = lector.nextLine();
                String[] campos = linea.split(",");
                String id = campos[0];
                String nombre = campos[1];
                String cantidad = campos[2];
                double precio_compra = Double.parseDouble(campos[3]);
                double precio_venta = Double.parseDouble(campos[4]);
                Producto producto = new Producto(id, nombre, cantidad, precio_compra, precio_venta);
                nuevaLista.add(producto);
            }
        } catch (FileNotFoundException ex) {
            System.out.println("El archivo no se encuentra");
            }
            this.productos = nuevaLista;
        }
    }


