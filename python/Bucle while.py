# en un ciclo while  crear un contador y en cada vuelta imprime un mensaje

cont = 1

while cont >= 10:
    print ("Hola MUndo  " , cont)
    cont  += 1 
    
#otro ejercicio para adivinar un numero

num = int(input("Digite un numero. "))

while num != 8:
    
    if num < 8:
        print("Numero menor digite nuevamente el numero.")
        num = int(input("Digite un numero. "))
    elif num >8:
        print("Numero mayor digite nuevamente el numero.")
        num = int(input("Digite un numero. "))
8
print("Adivinaste el numero.  ")        

