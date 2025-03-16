package java;

public class Condicionales {
    public static void main(String[] args) {
        int edad = 20;

        if (edad < 18) {
            System.out.println("Eres menor de edad.");
        } else if (edad >= 18 && edad < 65) {
            System.out.println("Eres un adulto.");
        } else {
            System.out.println("Eres un adulto mayor.");
        }
    }
    
}
