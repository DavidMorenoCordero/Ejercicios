#Definimos una lista con 10 elementos
mi_lista = [34 ,12, 45, 67, 23, 89, 5, 90, 56, 78]

#funcion que realiza varias operaciones sobre la lista
def operar_lista(lista):
    #ordena la lista de orden ascendente
    lista_ordenada = sorted(lista)
    print("lista ordenada: ", lista_ordenada)
    #Extraemos un rango de la lista del indice 2,6
    sub_lista = lista_ordenada[2:7]
    print("sublista indices 2 al 6: ", sub_lista)
    
    #creamos la lista con los elementos de la sublista
    nueva_lista = [x**2 for x  in sub_lista]
    print("nueva lista con elementos elevados al cuadrado: ", nueva_lista)
    #modificacion de la list origina remplazando el tercer elemnto
    lista_modificada = lista.copy()  #creamos una copia para no afectar la original
    lista_modificada[2] =100
    print("lista modificada ",  lista_modificada)
    
    return lista_ordenada, sub_lista, nueva_lista, lista_modificada
#llamamos a la funcion y almacenamos los resultados
ordenada, sub, nueva, modificada = operar_lista(mi_lista)