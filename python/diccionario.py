#diccionario inicial con varios datos
#se define un diccionario donde la clavees el id y el valor es otro diccionario con nombre y edad
registros = {
    
    1:{"nombre": "ana", "edad": 25},
    2:{"nombre": "luis", "edad": 30},
    3:{"nombre": "carlos", "edad": 22}
}

#funcion para consultar por nombre

def consultar(nombre):
    """
    Busca registros en el diccionario cuyo nombre coincida con el parametro dado (sin distinguir mayusculas/minusculas).
    : param nombre: Nombre a buscar.
    :return: Diccionario con los registros que coinciden.
    """
    return {id_: datos for id_, datos in registros.items() if datos["nombre"].lower()==nombre.lower()}

#funcion para ordenar el diccionario por clave

def ordenar_por_clave(clave):
    
    """
    Busca registros en el diccionario cuyo nombre coincida con el parametro dado (edad o nombre).
    : param nclave: clave por la cual ordenar.
    :return: lista de tuplas ordenadas.
    """
    return sorted(registros.items(), key=lambda x:x[1][clave])

# funcion para agregar un registro nuevo

def anexar_registro():
    """
    permite al usuario ingresar un nuevo registro mediaante la entrada de datospr teclado
    """
    
    id_nuevo = int(input("Ingrese el id: "))
    nombre_nuevo = input("Ingrese el nombre: ")
    edad_nueva = int(input("Ingrese la edad"))
    registros[id_nuevo] = {"nombre": nombre_nuevo, "edad": edad_nueva}
    print("registro agregado exitosamente. ")
    
    
def filtrar_por_edad(edad_minima):
    """
    Filtrar los registros cuya edad sea mayor o igual a la edad minima especificada
    :param edad_minima : Edad minima para filtrar.
    return: diccionario de registros filtrados.
    """
    return{id_: datos for id_, datos in registros.items() if datos["edad"]>=edad_minima}

def menu():
    while True:
        print("\n---MENU---")
        print("1. Consultar por nombre")
        print("2. ordenar  registros")
        print("3. Agregar nuevo registro")
        print("4. Filtar por edad")
        print("5. mostrar registros")
        print("6. salir")
        
        opcion = input("Selecionar una opcion: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombrea consultar: ")
            print("Resultados:", consultar(nombre))
        elif opcion == "2": 
            clave = input("Ingrese la clave de ordenamiento(nombre, edad): ")
            print("Registros ordenados: ", ordenar_por_clave(clave))
        elif opcion == "3":
            anexar_registro()
        elif opcion == "4":
            edad = int(input("ingrese la edad minima para filtrar: "))
            print("registros filtrados:",filtrar_por_edad(edad))
        elif opcion == "5":
            print("listacompleta de registros: " , registros)
        elif opcion == "6" : 
            print("saliendo del programa. ")
            break
        else:
            print("opcion no valida. intente de nuevo. ")
            
menu()