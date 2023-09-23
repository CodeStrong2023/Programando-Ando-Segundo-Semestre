/*
Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si
la fecha es corecta. Suponiedno que todos los meses son de
30 dias

*/

package Ciclos9;

import javax.swing.JOptionPane;

public class Ciclos9 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el dia: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes: "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el anio: "));
        
        if((dia != 0)&&(dia <= 30)){
            if((mes != 0)&&(mes <= 30)){
                if((anio != 0)&&(anio <= 30)){
                    JOptionPane.showMessageDialog(null, "La fecha ingresada es: "+dia+ "/"+mes+ "/"+anio);
                }
                else{
                    JOptionPane.showMessageDialog(null, "Fecha incorecta, anio incorrecto");
                }
            }
            else{
                JOptionPane.showMessageDialog(null, "Fecha incorecta, mes incorrecto");
            }
        }
        else{
            JOptionPane.showMessageDialog(null, "Fecha incorecta, dia incorrecto");
        } 
    }
}
