// Diccionario inicial con varios datos
let registros = {
    1: { "nombre": "ana", "edad": 25 },
    2: { "nombre": "luis", "edad": 30 },
    3: { "nombre": "carlos", "edad": 22 }
};

// Función para consultar por nombre
function consultar(nombre) {
    return Object.fromEntries(
        Object.entries(registros).filter(([id, datos]) => datos.nombre.toLowerCase() === nombre.toLowerCase())
    );
}

// Función para ordenar el diccionario por clave
function ordenarPorClave(clave) {
    return Object.entries(registros).sort((a, b) => a[1][clave] > b[1][clave] ? 1 : -1);
}

// Función para agregar un registro nuevo
function anexarRegistro() {
    const idNuevo = parseInt(prompt("Ingrese el id:"));
    const nombreNuevo = prompt("Ingrese el nombre:");
    const edadNueva = parseInt(prompt("Ingrese la edad:"));
    registros[idNuevo] = { "nombre": nombreNuevo, "edad": edadNueva };
    console.log("Registro agregado exitosamente.");
}

// Función para filtrar por edad
function filtrarPorEdad(edadMinima) {
    return Object.fromEntries(
        Object.entries(registros).filter(([id, datos]) => datos.edad >= edadMinima)
    );
}

// Función del menú
function menu() {
    while (true) {
        console.log("\n---MENU---");
        console.log("1. Consultar por nombre");
        console.log("2. Ordenar registros");
        console.log("3. Agregar nuevo registro");
        console.log("4. Filtrar por edad");
        console.log("5. Mostrar registros");
        console.log("6. Salir");

        const opcion = prompt("Seleccionar una opción:");

        if (opcion === "1") {
            const nombre = prompt("Ingrese el nombre a consultar:");
            console.log("Resultados:", consultar(nombre));
        } else if (opcion === "2") {
            const clave = prompt("Ingrese la clave de ordenamiento (nombre, edad):");
            console.log("Registros ordenados:", ordenarPorClave(clave));
        } else if (opcion === "3") {
            anexarRegistro();
        } else if (opcion === "4") {
            const edad = parseInt(prompt("Ingrese la edad mínima para filtrar:"));
            console.log("Registros filtrados:", filtrarPorEdad(edad));
        } else if (opcion === "5") {
            console.log("Lista completa de registros:", registros);
        } else if (opcion === "6") {
            console.log("Saliendo del programa.");
            break;
        } else {
            console.log("Opción no válida. Intente de nuevo.");
        }
    }
}

// Llamar a la función del menú
menu();