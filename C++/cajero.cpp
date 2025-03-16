#include <iostream>
using namespace std;

int main() {
    double saldo = 1000.0; // Saldo inicial
    int opcion;
    
    do {
        cout << "Bienvenido al Cajero Automático" << endl;
        cout << "1. Consultar saldo" << endl;
        cout << "2. Retirar dinero" << endl;
        cout << "3. Depositar dinero" << endl;
        cout << "4. Salir" << endl;
        cout << "Seleccione una opción: ";
        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "Su saldo es: $" << saldo << endl;
                break;
            case 2: {
                double retiro;
                cout << "Ingrese la cantidad a retirar: ";
                cin >> retiro;
                if (retiro > saldo) {
                    cout << "Fondos insuficientes." << endl;
                } else {
                    saldo -= retiro;
                    cout << "Retiro exitoso. Su nuevo saldo es: $" << saldo << endl;
                }
                break;
            }
            case 3: {
                double deposito;
                cout << "Ingrese la cantidad a depositar: ";
                cin >> deposito;
                saldo += deposito;
                cout << "Depósito exitoso. Su nuevo saldo es: $" << saldo << endl;
                break;
            }
            case 4:
                cout << "Gracias por usar el cajero automático." << endl;
                break;
            default:
                cout << "Opción no válida. Intente de nuevo." << endl;
        }
    } while (opcion != 4);

    return 0;
}