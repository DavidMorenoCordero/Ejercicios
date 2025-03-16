package java;

public class Variables {
    public static void main(String[] args) {
        String nombre = "Carlos";
        int edad = 25;
        double precio = 199.99;
        boolean activo = true;

        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad + " años");
        System.out.println("Precio: $" + precio);
        System.out.println("Estado activo: " + (activo ? "Sí" : "No"));
    }
}
