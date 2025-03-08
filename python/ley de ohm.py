def ley_de_ohm():
    print("Calculadora de la Ley de Ohm")
    print("Seleccione la variable que desea calcular:")
    print("1. Tensión (V)")
    print("2. Corriente (I)")
    print("3. Resistencia (R)")

    opcion = input("Ingrese el número de la opción (1/2/3): ")

    if opcion == '1':
        # Calcular Tensión (V)
        I = float(input("Ingrese la corriente (I) en amperios: "))
        R = float(input("Ingrese la resistencia (R) en ohmios: "))
        V = I * R
        print(f"La tensión (V) es: {V} voltios")

    elif opcion == '2':
        # Calcular Corriente (I)
        V = float(input("Ingrese la tensión (V) en voltios: "))
        R = float(input("Ingrese la resistencia (R) en ohmios: "))
        I = V / R
        print(f"La corriente (I) es: {I} amperios")

    elif opcion == '3':
        # Calcular Resistencia (R)
        V = float(input("Ingrese la tensión (V) en voltios: "))
        I = float(input("Ingrese la corriente (I) en amperios: "))
        R = V / I
        print(f"La resistencia (R) es: {R} ohmios")

    else:
        print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

# Llamar a la función
ley_de_ohm()