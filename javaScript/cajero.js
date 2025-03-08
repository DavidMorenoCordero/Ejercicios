class Cajero {
    constructor(nombre, numeroCuenta, saldo) {
        this.nombre = nombre;
        this.numeroCuenta = numeroCuenta;
        this.saldo = saldo;
    }

    // Función para realizar depósitos
    Deposito(cantidad) {
        this.saldo += cantidad;
        console.log(`Has guardado: ${cantidad}. Nuevo saldo: ${this.saldo}`);
    }

    // Función para realizar retiros
    Retiros(cantidad) {
        if (cantidad > this.saldo) {
            console.log("Fondos insuficientes...");
        } else {
            this.saldo -= cantidad;
            console.log(`Has retirado: ${cantidad}. Nuevo saldo: ${this.saldo}`);
        }
    }

    // Función para realizar transferencias
    Transferencias(cantidad, cuentaDestino) {
        if (cantidad > this.saldo) {
            console.log("Fondos insuficientes...");
        } else {
            this.saldo -= cantidad;
            cuentaDestino.Deposito(cantidad);
            console.log(`Has transferido a ${cuentaDestino.nombre} la cantidad: ${cantidad}. Saldo actual: ${this.saldo}`);
        }
    }
}

// Función principal
function main() {
    // Solicitar datos
    const nombre = prompt("Ingresa tu nombre:");
    const numeroCuenta = prompt("Ingresa tu número de cuenta:");
    const saldo = parseFloat(prompt("Ingresa tu saldo inicial:"));

    const cajero = new Cajero(nombre, numeroCuenta, saldo);

    while (true) {
        console.log("\nOpciones:");
        console.log("1. Depósitos.");
        console.log("2. Retiros.");
        console.log("3. Transferencias.");
        console.log("4. Ver saldo.");
        console.log("5. Salir.");

        const opcion = prompt("Selecciona una opción:");

        if (opcion === '1') {
            const cantidad = parseFloat(prompt("Ingresa la cantidad a ingresar:"));
            cajero.Deposito(cantidad);
        } else if (opcion === '2') {
            const cantidad = parseFloat(prompt("Ingresa la cantidad a retirar:"));
            cajero.Retiros(cantidad);
        } else if (opcion === '3') {
            const cantidad = parseFloat(prompt("Ingresa la cantidad a transferir:"));
            const numeroCuentaDestino = prompt("Ingresa el número de la cuenta de destino:");
            const cuentaDestino = new Cajero("Usuario Destino", numeroCuentaDestino, 0);
            cajero.Transferencias(cantidad, cuentaDestino);
        } else if (opcion === '4') {
            console.log(`Tu saldo es: ${cajero.saldo}`);
        } else if (opcion === '5') {
            console.log("Gracias por usar el cajero automático.");
            break; // Salir del bucle
        } else {
            console.log("Opción no válida, intenta de nuevo.");
        }
    }
}

// Llamar a la función principal
main();