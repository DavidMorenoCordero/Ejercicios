#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<string> nombres;
    string nombre;
    char continuar;

    do {
        cout << "Ingrese un nombre: ";
        cin >> nombre;
        nombres.push_back(nombre);
        cout << "¿Desea agregar otro nombre? (s/n): ";
        cin >> continuar;
    } while (continuar == 's' || continuar == 'S');

    cout << "Los nombres ingresados son:" << endl;
    for (const auto& n : nombres) {
        cout << n << endl;
    }

    return 0;
}