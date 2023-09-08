
package CicloWhile;


public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0;
        while (conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo ++;
        }
        
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
    }
}
