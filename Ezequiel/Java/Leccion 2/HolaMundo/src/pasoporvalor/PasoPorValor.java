
package pasoporvalor;
/*
Los parámetros por valor son una forma de pasar datos a una función o procedimiento 
donde se copia el valor actual de la variable o argumento al parámetro de la función. 
Esto significa que cualquier cambio realizado en el parámetro dentro de la función 
no afectará la variable original fuera de la función.
*/

public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("valorX = " + valorX);
        
        cambioValor(valorX);
        System.out.println("valorX = " + valorX);
    }
    
    public static void cambioValor(int arg1){
        System.out.println("arg1 = " + arg1);
        arg1 = 15; //No va a cambiar el valor de arg1
    }
}
