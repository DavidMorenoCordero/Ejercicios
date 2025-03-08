function tablaDeVerdad() {
    console.log("A\tB\tA AND B\tA OR B\tNOT A\tNOT B");
    console.log("-".repeat(40));

    // Iterar sobre todas las combinaciones de A y B
    for (let A of [true, false]) {
        for (let B of [true, false]) {
            const andResult = A && B;
            const orResult = A || B;
            const notA = !A;
            const notB = !B;

            // Imprimir los resultados
            console.log(`${A}\t${B}\t${andResult}\t${orResult}\t${notA}\t${notB}`);
        }
    }
}