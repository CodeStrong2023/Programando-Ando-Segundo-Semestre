public class EjercicioWhile {
    public static void main(String[] args) {
        /*Cilo While */

        /*var conteo = 0;  // Inferencia de tipos
        while(conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
        }


        /* Ciclo Do While */
        /* 
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;   // Aplicar siempre un contador para que el ciclo tenga un FIN.
        }while(contador <= 7);


        /* Ciclo For */
        // Uso de las palabras break y continue junto a las etiquetas (labels)
        /* Metodo Break */
    
        for (var contando = 0; contando <7; contando++){
            if(contando %  2 == 0) {
                System.out.println("contando = " +contando);
                break;
 
            }
            
        }
        
        /* Metodo Continue */
        inicio:
        for (var contando = 0; contando <7; contando++){
            if(contando %  2 != 0) { 
                continue inicio; //Vamos a la siguiente iteracion
            }
            System.out.println("contando = " +contando);
        }

        

        

   
    }

}