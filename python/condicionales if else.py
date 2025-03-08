# un programa para verificar si un numero es positivo o negativo

num = float(input("Ingrese un numero: "))

if num > 0 :
    print("El numero es positivo.")
elif num < 0 :
    print("El numero es negativos.")
else:
    print("el numero es cero.")
    
#calcular la calificacion de un estudiante

calificacion = float(input("Ingrese la caliificacion del estudiante: "))

if calificacion >= 90:
    print("Calificacion Excelente: E.")
elif calificacion >= 80:
    print ("Calificaion es Sobresaliente: S.")
elif calificacion >=60:
    print("Calificacion es aceptable: A.")
elif calificacion >=40:
    print("Calificacion es Insuficiente: I.")
else: 
    print("Calificacion Defisiente: D.")