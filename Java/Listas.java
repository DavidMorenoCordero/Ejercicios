package java;

import java.util.ArrayList;

public class Listas {
    
    public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<>();
        numeros.add(10);
        numeros.add(20);
        numeros.add(30);
        numeros.add(40);
        numeros.add(50);

        System.out.println("Lista de números:");
        for (int num : numeros) {
            System.out.println(num);
        }

        // Agregar un número
        numeros.add(60);
        System.out.println("Nueva lista con 60 añadido: " + numeros);
    }
}
