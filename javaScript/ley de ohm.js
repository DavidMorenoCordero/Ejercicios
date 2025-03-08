function leyDeOhm() {
    console.log("Calculadora de la Ley de Ohm");
    console.log("Seleccione la variable que desea calcular:");
    console.log("1. Tensión (V)");
    console.log("2. Corriente (I)");
    console.log("3. Resistencia (R)");

    let opcion = prompt("Ingrese el número de la opción (1/2/3):");

    if (opcion === '1') {
        // Calcular Tensión (V)
        let I = parseFloat(prompt("Ingrese la corriente (I) en amperios:"));
        let R = parseFloat(prompt("Ingrese la resistencia (R) en ohmios:"));
        let V = I * R;
        console.log(`La tensión (V) es: ${V} voltios`);

    } else if (opcion === '2') {
        // Calcular Corriente (I)
        let V = parseFloat(prompt("Ingrese la tensión (V) en voltios:"));
        let R = parseFloat(prompt("Ingrese la resistencia (R) en ohmios:"));
        let I = V / R;
        console.log(`La corriente (I) es: ${I} amperios`);

    } else if (opcion === '3') {
        // Calcular Resistencia (R)
        let V = parseFloat(prompt("Ingrese la tensión (V) en voltios:"));
        let I = parseFloat(prompt("Ingrese la corriente (I) en amperios:"));
        let R = V / I;
        console.log(`La resistencia (R) es: ${R} ohmios`);

    } else {
        console.log("Opción no válida. Por favor, seleccione 1, 2 o 3.");
    }
}

// Llamar a la función
leyDeOhm();