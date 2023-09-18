package cicloWhile;

public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0;
        /*while(conteo <7){
            System.out.println("conteo = " + conteo);
            conteo++;
        }*/
        /*
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador<7);
        */
        //USo de brrak y continue y de etiquetas (labels)
        for(var contador = 0; contador<7; contador++){
            if (contador % 2 ==0) {
                System.out.println("contador = " + contador);
                break;
            }
        }
        inicio:
        for(var contador = 0; contador<7; contador++){
            if (contador % 2 !=0) {
               continue inicio;                
            }
            System.out.println("contador = " + contador);
        }
    }
}
