#en este ejercicio realizaremos un sistema de cajeros sisples en donde tengamos la funciones mas basicas de un cajero

#Creamos la clase de cajero

class Cajero: 
      #definimos la funcion de inicio para la toma de datos iniciales
    def __inicio__ (self, nombre, numeroCuenta, saldo):
        self.nombre = nombre
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
      # definimos la funcion para los depositos o ingresos de dinero  
    def Deposito(self, cantidad):
        self.saldo += cantidad
        print(f"Has Guardado. " , cantidad , " Nuevo Saldo: ", self.saldo)
     # definimos la funcion para los retiros   
    def Retiros(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes...")
        else:
            self.saldo -= cantidad
            print(f"Has Retirado. " , cantidad , " Nuevo Saldo: ", self.saldo)
      #definimos la funcion para realizar las trnsferecnias      
    def Transferencias(self,cantidad, cuenta_destino):
        if cantidad >self.saldo:
            print("Fondos insuficientes...")
        else:
            self.saldo -= cantidad
            cuenta_destino.Deposito(cantidad)
            print(f"Has Transferido a . " , cuenta_destino , " El siguiente dinero: ", cantidad , "Saldo Actual. ", self.saldo)
            
#Aqui realizaremos la funcion principal

def main():
    #Solicitmos datos
    nombre = input("Ingresa tu nombre:  ")
    numeroCuenta  = input("Ingresa tu numero de cuenta:  ")
    saldo =float(input("Ingresa tu saldo Inicial:  "))
      
    Cajero = Cajero(nombre, numeroCuenta, saldo)
    
    while True:
        print("\n Opciones: ")
        print("1. Depositos.")
        print("2. Retiros.")
        print("3. Transferencias.")
        print("4. Ver Saldo.")
        print("5. Salir.")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == '1':
            cantidad = float(input("Ingresa la cantidad a ingresar: "))
            Cajero.Depositos(cantidad)
        elif opcion =='2':
            cantidad = float(input("Ingresa la cantidad a retirar: "))
            Cajero.Retiros(cantidad)
        elif opcion =='3':
            cantidad = float(input("Ingresa la cantidad a transferir: "))
            numeroCuentaDestino = input("Ingresa el numero de la cuenta de destino: ")
            cuentaDestino = Cajero("Usuario Destino", numeroCuentaDestino,0)
            Cajero.TranferenciasDinero(cantidad, cuentaDestino)
            
        elif opcion=='4':
            print("Tu Saldo es: ....",Cajero.saldo)
        elif opcion=='5':
            print("Gracias por usar el cajero automatico.")
        else: 
            print("Opcion no valida, Intente de Nuevo.")
            
if Cajero.__inicio__ == "__main__":
    main()
    