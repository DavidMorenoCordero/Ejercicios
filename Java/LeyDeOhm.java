package java;

import java.util.Scanner;

public class LeyDeOhm {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese voltaje (V) o 0 si no lo sabe: ");
        double voltaje = scanner.nextDouble();
        System.out.print("Ingrese corriente (I) o 0 si no lo sabe: ");
        double corriente = scanner.nextDouble();
        System.out.print("Ingrese resistencia (R) o 0 si no lo sabe: ");
        double resistencia = scanner.nextDouble();

        if (voltaje == 0 && corriente != 0 && resistencia != 0) {
            voltaje = corriente * resistencia;
            System.out.println("El voltaje es: " + voltaje + " V");
        } else if (corriente == 0 && voltaje != 0 && resistencia != 0) {
            corriente = voltaje / resistencia;
            System.out.println("La corriente es: " + corriente + " A");
        } else if (resistencia == 0 && voltaje != 0 && corriente != 0) {
            resistencia = voltaje / corriente;
            System.out.println("La resistencia es: " + resistencia + " Ω");
        } else {
            System.out.println("Debe dejar un valor como 0 para calcularlo.");
        }

        scanner.close();
    }
}
