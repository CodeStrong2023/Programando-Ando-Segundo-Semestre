/*
Ejercicio 11: Diseñar un programa que muestre el producto de los primeros 11 numeros impares
Usar la clase JOptionPane
*/
package ciclos11;

public class Ciclos11 {
    public static void main(String[] args) {
        int resultado = 1;
        int contador = 0;
        int numero = 1;
        while (contador < 11){
            if(numero % 2 != 0){
                resultado *= numero;
                contador++;
            }
            numero++;
        }
        System.out.println("El resultado  de la operacion es: " + resultado);
    }   
}
