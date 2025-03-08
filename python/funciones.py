def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def divicion (a, b):
    return a / b

def potencia (a, b):
    return a ** b

def calculador():
    while True:
        print("\n---Calculadora en python---")
        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. divicion")
        print("5. potenciacion")
        print("6. Salir")
        
        opcion = input("Selecione una opcion (1-6): ")
        
        if opcion == "6":
            print("Saliendo de la calculadora...")
            break
        
        if opcion not in ["1","2","3","4","5","6"]:
            print("Opcion no valida. Intente de nueevo. ")
            continue
        
        try:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            
            operaciones = {
                "1" : suma,
                "2" :resta,
                "3" : multiplicacion,
                "4" : divicion,
                "5" : potencia
            }
            
            resutado = operaciones[opcion](num1, num2)
            print (f"resultado: {resutado}")
            
        except ValueError:
                print("Error: Ingrese solo numerosvalidos. ")
calculador()
    


