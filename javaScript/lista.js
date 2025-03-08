// Definimos una lista con 10 elementos
let miLista = [34, 12, 45, 67, 23, 89, 5, 90, 56, 78];

// Función que realiza varias operaciones sobre la lista
function operarLista(lista) {
    // Ordena la lista de orden ascendente
    let listaOrdenada = lista.slice().sort((a, b) => a - b); // Usamos slice() para no modificar la lista original
    console.log("Lista ordenada:", listaOrdenada);

    // Extraemos un rango de la lista del índice 2 al 6
    let subLista = listaOrdenada.slice(2, 7);
    console.log("Sublista índices 2 al 6:", subLista);

    // Creamos la lista con los elementos de la sublista elevados al cuadrado
    let nuevaLista = subLista.map(x => x ** 2);
    console.log("Nueva lista con elementos elevados al cuadrado:", nuevaLista);

    // Modificación de la lista original reemplazando el tercer elemento
    let listaModificada = lista.slice(); // Creamos una copia para no afectar la original
    listaModificada[2] = 100;
    console.log("Lista modificada:", listaModificada);

    return { listaOrdenada, subLista, nuevaLista, listaModificada };
}

// Llamamos a la función y almacenamos los resultados
let { listaOrdenada, subLista, nuevaLista, listaModificada } = operarLista(miLista);