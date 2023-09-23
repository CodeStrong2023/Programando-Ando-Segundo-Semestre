
package ejerciciowhile01;

public class EjercicioWhile01 {

    public static void main(String[] args) {

        var conteo = 0;
        while(conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo ++;
        }
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador<7);
        
        inicio: //Etiqueta (label)
        for(var contar = 0;contar<7;contar++){
            if(contar % 2 ==0){
                continue inicio;
            }
            System.out.println("contar = " + contar);
        }
        
        
    }
    
}
