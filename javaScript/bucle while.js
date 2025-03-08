let cont = 1;

while (cont <= 10) {
    console.log("Hola Mundo " + cont);
    cont += 1; // Incrementar el contador
}

//otro ejercicio

let num = parseInt(prompt("Digite un número."));

while (num !== 8) {
    if (num < 8) {
        console.log("Número menor, digite nuevamente el número.");
    } else if (num > 8) {
        console.log("Número mayor, digite nuevamente el número.");
    }
    num = parseInt(prompt("Digite un número."));
}

console.log("Adivinaste el número.");