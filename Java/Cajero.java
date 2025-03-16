package java;

import java.util.Scanner;

public class caja {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double saldo = 1000.0; // Saldo inicial

        while (true) {
            System.out.println("\n=== Cajero Automático ===");
            System.out.println("1. Consultar saldo");
            System.out.println("2. Depositar dinero");
            System.out.println("3. Retirar dinero");
            System.out.println("4. Salir");
            System.out.print("Elige una opción: ");
            
            int opcion = scanner.nextInt();

            if (opcion == 1) {
                System.out.println("Tu saldo actual es: $" + saldo);
            } else if (opcion == 2) {
                System.out.print("Ingresa el monto a depositar: ");
                double deposito = scanner.nextDouble();
                if (deposito > 0) {
                    saldo += deposito;
                    System.out.println("Depósito exitoso. Tu nuevo saldo es: $" + saldo);
                } else {
                    System.out.println("Monto inválido.");
                }
            } else if (opcion == 3) {
                System.out.print("Ingresa el monto a retirar: ");
                double retiro = scanner.nextDouble();
                if (retiro > 0 && retiro <= saldo) {
                    saldo -= retiro;
                    System.out.println("Retiro exitoso. Tu nuevo saldo es: $" + saldo);
                } else {
                    System.out.println("Fondos insuficientes o monto inválido.");
                }
            } else if (opcion == 4) {
                System.out.println("Gracias por usar el cajero. ¡Hasta luego!");
                break; // Salir del bucle
            } else {
                System.out.println("Opción inválida. Intenta de nuevo.");
            }
        }

        scanner.close();
    }
}
