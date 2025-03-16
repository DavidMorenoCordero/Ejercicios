package java;

import java.util.HashMap;

public class Diccionario {
    
    public static void main(String[] args) {
        HashMap<String, String> persona = new HashMap<>();
        persona.put("nombre", "Carlos");
        persona.put("edad", "25");
        persona.put("ciudad", "Bogotá");

        // Acceder a valores
        System.out.println("Nombre: " + persona.get("nombre"));
        System.out.println("Edad: " + persona.get("edad"));
        System.out.println("Ciudad: " + persona.get("ciudad"));
    }
}
