package java;

import java.util.Scanner;

public class InteraccionUsuario {
    
public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa tu nombre: ");
        String nombre = scanner.nextLine();

        System.out.println("Hola, " + nombre + ". ¡Bienvenido!");
        scanner.close();
    }

}
