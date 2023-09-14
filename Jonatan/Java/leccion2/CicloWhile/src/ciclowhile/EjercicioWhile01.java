
package ciclowhile;
public class EjercicioWhile01 {
    public static void main(String[] args) {
        
        //CICLO WHILE "MIENTRAS"
        var conteo = 0;//inferencia de tipos
        while (conteo <= 7){
            System.out.println("Conteo = "+ conteo);
            conteo++; // aumenta + 1 la variable conteo
        }
        
        
        //La diferencia entre ambos es que, en el bucle while, la condición 
        //booleana se evalúa antes de que se ejecute el código. En cambio, 
        //en un bucle do-while primero se ejecuta una vez el código (do) y, a continuación,
        //se evalúa la condición. Si esta no se cumple, el hilo de ejecución sale del bucle.
        
        //CICLO DO WHILE "MIENTRAS HACER"
        
        var contador = 0;//inicio la variable en 0
         do{
            System.out.println("contador = " + contador);
           contador++;//aumentamos el contador cada vez que re repita el ciclo
            
         }while(contador <=7);
        
        //CICLO FOR "PARA"  ciclo for es una estructura iterativa para ejecutar un mismo
        //segmento de código una cantidad de veces deseada; conociendo previamente un valor de inicio
        
        //for("declarar o crear variable";"Condicion";"Incremento o decremento")
        //si solo tenemos una linea de cod no es necesario las llaves.{}
        for(var contando = 0; contando < 7 ; contando++){
            if(contando % 2 ==0){
            System.out.println("contando = " + contando);
            //el break sirve para detener "Romper" el ciclo cuiando encuentra el resultado.
            break;
            }
        }
        //ETIQUETAS LABELS
        inicio:
        for(var contando = 0; contando < 7 ; contando++){
            if(contando % 2 !=0){
                continue inicio; //Vamos a la siguiente iteracion
            }
            System.out.println("contando = " + contando);
        }
        
       
        
               
     }  
}
