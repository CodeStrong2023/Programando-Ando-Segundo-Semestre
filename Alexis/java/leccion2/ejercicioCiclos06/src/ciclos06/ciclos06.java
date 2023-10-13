/*
ejercicio 6: pedir numeros hasta que se teclee un 0, mostrar
la suma de todos los numeros introducidos
*/
package ciclos06;


public class ciclos06 {
    public static void main(String[] args) {
        int numero,suma = 0;
        do{
            System.out.println("digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma+= numero;
        }while(numero != 0);
        System.out.println("\n La suma de todos los numeros ingresados es: "+suma);
    }
}
