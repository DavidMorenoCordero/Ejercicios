// Solicitar la calificación del estudiante
let calificacion = parseFloat(prompt("Ingrese la calificación del estudiante:"));

// Evaluar la calificación y mostrar el resultado
if (calificacion >= 90) {
    console.log("Calificación Excelente: E.");
} else if (calificacion >= 80) {
    console.log("Calificación Sobresaliente: S.");
} else if (calificacion >= 60) {
    console.log("Calificación Aceptable: A.");
} else if (calificacion >= 40) {
    console.log("Calificación Insuficiente: I.");
} else {
    console.log("Calificación Deficiente: D.");
}