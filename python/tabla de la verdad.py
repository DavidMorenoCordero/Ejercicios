def tabla_de_verdad():
    print("A\tB\tA AND B\tA OR B\tNOT A\tNOT B")
    print("-" * 40)

    # Iterar sobre todas las combinaciones de A y B
    for A in [True, False]:
        for B in [True, False]:
            and_result = A and B
            or_result = A or B
            not_A = not A
            not_B = not B
            
            # Imprimir los resultados
            print(f"{A}\t{B}\t{and_result}\t{or_result}\t{not_A}\t{not_B}")

# Llamar a la función
tabla_de_verdad()