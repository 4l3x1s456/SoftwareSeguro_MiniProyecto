#include <iostream>
#include "entrenar_modelo.h"
#include "usar_modelo.h"

using namespace mlpack;
using namespace arma;
using namespace std;

void mostrar_menu() {
	system("cls");
    cout << "\n=== SISTEMA DE DETECCION DE VULNERABILIDADES ===\n";
    cout << "1. Entrenar modelo\n";
    cout << "2. Usar modelo (predecir ejemplo)\n";
    cout << "3. Analizar codigo_vulnerable_demo.py\n";
    cout << "4. Salir\n";
    cout << "Seleccione una opcion: ";
}

int main()
{
    int opcion;
    
    do {
        mostrar_menu();
        cin >> opcion;
        
        switch(opcion) {
            case 1:
            	system("cls");
                cout << "\nEntrenando modelo...\n";
                try {
                    entrenar_modelo_mineriadatos();
                } catch(const exception& e) {
                    cerr << "Error al entrenar el modelo: " << e.what() << endl;
                }
                system("pause");
                break;
                
            case 2:
            	system("cls");
                cout << "\nUsando modelo para prediccion...\n";
                try {
                    usar_modelo_mineriadatos();
                } catch(const exception& e) {
                    cerr << "Error al usar el modelo: " << e.what() << endl;
                }
                system("pause");
                break;
                
            case 3:
            	system("cls");
                cout << "\nAnalizando codigo_vulnerable_demo.py...\n";
                try {
                    cout << "Extrayendo caracteristicas del codigo vulnerable...\n";
                    system("C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe analizar_codigo_vulnerable.py");
                    cout << "\nAhora analizando con el modelo...\n";
                    usar_modelo_mineriadatos();
                } catch(const exception& e) {
                    cerr << "Error al analizar el codigo: " << e.what() << endl;
                }
                system("pause");
                break;
                
            case 4:
            	system("cls");
                cout << "\nSaliendo del programa...\n";
                break;
                
            default:
                cout << "\nOpcion invalida. Por favor seleccione 1, 2, 3 o 4.\n";
                system("pause");
        }
        
    } while(opcion != 4);
    
    return 0;
}
