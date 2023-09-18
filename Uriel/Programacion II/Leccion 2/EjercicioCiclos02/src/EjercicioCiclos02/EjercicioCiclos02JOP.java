package EjercicioCiclos02;

import javax.swing.JOptionPane;

public class EjercicioCiclos02JOP {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(numero != 0){
            if (numero > 0) {
                System.out.println("El numero " +numero+ " es positivo");
            }
            else{
                System.out.println("El numero " +numero+ " es negativo");
            }
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        System.out.println("El numero "+numero+" finaliza el programa");
    }
}
