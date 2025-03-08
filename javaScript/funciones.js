// Funciones para las operaciones
function suma(a, b) {
    return a + b;
}

function resta(a, b) {
    return a - b;
}

function multiplicacion(a, b) {
    return a * b;
}

function division(a, b) {
    return a / b;
}

function potencia(a, b) {
    return Math.pow(a, b);
}

// Función de la calculadora
function calculador() {
    while (true) {
        console.log("\n--- Calculadora en JavaScript ---");
        console.log("1. Suma");
        console.log("2. Resta");
        console.log("3. Multiplicación");
        console.log("4. División");
        console.log("5. Potenciación");
        console.log("6. Salir");

        const opcion = prompt("Seleccione una opción (1-6):");

        if (opcion === "6") {
            console.log("Saliendo de la calculadora...");
            break;
        }

        if (!["1", "2", "3", "4", "5", "6"].includes(opcion)) {
            console.log("Opción no válida. Intente de nuevo.");
            continue;
        }

        try {
            const num1 = parseFloat(prompt("Ingrese el primer número:"));
            const num2 = parseFloat(prompt("Ingrese el segundo número:"));

            const operaciones = {
                "1": suma,
                "2": resta,
                "3": multiplicacion,
                "4": division,
                "5": potencia
            };

            const resultado = operaciones[opcion](num1, num2);
            console.log(`Resultado: ${resultado}`);

        } catch (error) {
            console.log("Error: Ingrese solo números válidos.");
        }
    }
}

// Llamar a la función de la calculadora
calculador();