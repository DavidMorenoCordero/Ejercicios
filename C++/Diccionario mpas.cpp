#include <iostream>
#include <map>
using namespace std;

int main() {
    map<string, int> edades;
    string nombre;
    int edad;
    char continuar;

    do {
        cout << "Ingrese el nombre: ";
        cin >> nombre;
        cout << "Ingrese la edad: ";
        cin >> edad;
        edades[nombre] = edad; // Almacena la edad en el mapa
       