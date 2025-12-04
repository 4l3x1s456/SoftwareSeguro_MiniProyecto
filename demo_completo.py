#!/usr/bin/env python3
"""
DEMOSTRACIÓN COMPLETA DEL SISTEMA DE DETECCIÓN DE VULNERABILIDADES
Muestra el flujo completo: análisis local + GitHub Actions
"""

import os
import subprocess
import sys


def mostrar_menu():
    """Muestra el menú principal de demostración"""
    print("\n" + "=" * 70)
    print("🔒 SISTEMA DE DETECCIÓN DE VULNERABILIDADES - DEMOSTRACIÓN COMPLETA")
    print("=" * 70)
    print("1. 🐍 Analizar código vulnerable con Python")
    print("2. ⚡ Analizar código vulnerable con modelo C++")
    print("3. 🚀 Simular detección en GitHub Actions")
    print("4. 📊 Ver flujo completo del sistema")
    print("5. 🔄 Ejecutar demo completo automático")
    print("6. 🚪 Salir")
    print("-" * 70)


def analizar_con_python():
    """Opción 1: Análisis con Python"""
    print("\n🐍 ANÁLISIS CON PYTHON")
    print("=" * 50)

    print("📄 Extrayendo características del código vulnerable...")
    result = os.system(
        "C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe analizar_codigo_vulnerable.py"
    )

    if result == 0:
        print("\n📊 Generando reporte con modelo Python...")
        os.system(
            "C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe demo_vulnerabilities.py"
        )

        print("\n✅ Análisis Python completado!")
        print("📁 Revisa: example_features.csv y demo_summary.json")
    else:
        print("❌ Error en el análisis Python")


def analizar_con_cpp():
    """Opción 2: Análisis con modelo C++"""
    print("\n⚡ ANÁLISIS CON MODELO C++")
    print("=" * 50)

    # Primero extraer características
    print("📄 Paso 1: Extrayendo características...")
    result = os.system(
        "C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe analizar_codigo_vulnerable.py"
    )

    if result != 0:
        print("❌ Error extrayendo características")
        return

    print("\n🤖 Paso 2: Ejecutando modelo C++...")
    print(
        "ℹ️ Selecciona la opción 3 en el menú para analizar el código vulnerable"
    )

    # Ejecutar el programa C++
    os.system("./Modelo_MineriaDatos.exe")


def simular_github_actions():
    """Opción 3: Simular GitHub Actions"""
    print("\n🚀 SIMULACIÓN DE GITHUB ACTIONS")
    print("=" * 50)

    print("📄 Paso 1: Extrayendo características de cambios...")
    result1 = os.system(
        "C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe scripts/extract_features_from_diff.py"
    )

    print("\n📊 Paso 2: Generando reporte de vulnerabilidades...")
    result2 = os.system(
        "C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe scripts/generate_basic_report.py"
    )

    if result1 == 0 and result2 == 0:
        print("\n✅ Simulación de GitHub Actions completada!")
        print("📁 Revisa el directorio reports/ para ver los resultados:")
        print("   • reports/vulnerability_report.html")
        print("   • reports/vulnerability_summary.json")
        print("   • reports/feature_importance.png")

        # Abrir el reporte si existe
        if os.path.exists("reports/vulnerability_report.html"):
            print("\n🌐 Abriendo reporte HTML...")
            os.system("start reports/vulnerability_report.html")
    else:
        print("❌ Error en la simulación")


def mostrar_flujo_completo():
    """Opción 4: Mostrar flujo del sistema"""
    print("\n📊 FLUJO COMPLETO DEL SISTEMA")
    print("=" * 70)

    flujo = """
🔄 ARQUITECTURA Y FLUJO DEL SISTEMA:

1️⃣ PREPARACIÓN DE DATOS (Python)
   └── preprocesar_vulnerabilidades.py
   └── Extrae características de datasets → train_features.csv

2️⃣ ENTRENAMIENTO (C++ + MLPack)  
   └── entrenar_modelo.h → Random Forest → rf_vuln_model.bin

3️⃣ ANÁLISIS LOCAL (Híbrido Python + C++)
   └── codigo_vulnerable_demo.py (TU CÓDIGO EDITABLE)
   └── analizar_codigo_vulnerable.py → example_features.csv  
   └── usar_modelo.h → Predicción + Alertas

4️⃣ INTEGRACIÓN CI/CD (Python + GitHub Actions)
   └── Git diff → extract_features_from_diff.py
   └── Modelo → generate_basic_report.py → Reportes HTML
   └── Comentarios automáticos en PRs

🎯 PUNTOS CLAVE:
• codigo_vulnerable_demo.py = Tu laboratorio de vulnerabilidades
• Detección automática en commits/PRs
• Alertas por probabilidades (>70% = crítico)
• Reportes con interpretabilidad

📁 ARCHIVOS PRINCIPALES:
• C++: main.cpp, entrenar_modelo.h, usar_modelo.h  
• Python: scripts/*.py, codigo_vulnerable_demo.py
• CI/CD: .github/workflows/vulnerability-detection.yml
    """

    print(flujo)


def ejecutar_demo_completo():
    """Opción 5: Demo automático completo"""
    print("\n🔄 DEMO AUTOMÁTICO COMPLETO")
    print("=" * 70)

    steps = [
        ("📄 Analizando código vulnerable",
         "C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe analizar_codigo_vulnerable.py"
         ),
        ("🐍 Ejecutando demo Python",
         "C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe demo_vulnerabilities.py"
         ),
        ("🚀 Simulando GitHub Actions",
         "C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe scripts/extract_features_from_diff.py"
         ),
        ("📊 Generando reportes",
         "C:/Users/alexi/AppData/Local/Programs/Python/Python311/python.exe scripts/generate_basic_report.py"
         )
    ]

    for i, (descripcion, comando) in enumerate(steps, 1):
        print(f"\n{i}/4 {descripcion}...")
        print("-" * 50)

        result = os.system(comando)

        if result == 0:
            print(f"✅ Paso {i} completado exitosamente")
        else:
            print(f"⚠️ Paso {i} completado con advertencias")

        input("📋 Presiona Enter para continuar...")

    print("\n🎉 DEMO COMPLETO FINALIZADO!")
    print("=" * 70)
    print("📁 Resultados generados:")
    print("   • example_features.csv (para modelo C++)")
    print("   • reports/vulnerability_report.html")
    print("   • reports/vulnerability_summary.json")
    print("   • demo_summary.json")

    print(f"\n🎯 PRÓXIMO PASO:")
    print("   Ejecuta ./Modelo_MineriaDatos.exe y selecciona opción 3")
    print("   para ver el análisis del modelo C++")


def main():
    """Función principal del sistema de demostración"""

    while True:
        mostrar_menu()

        try:
            opcion = input("Selecciona una opción (1-6): ").strip()

            if opcion == "1":
                analizar_con_python()
            elif opcion == "2":
                analizar_con_cpp()
            elif opcion == "3":
                simular_github_actions()
            elif opcion == "4":
                mostrar_flujo_completo()
            elif opcion == "5":
                ejecutar_demo_completo()
            elif opcion == "6":
                print("\n👋 ¡Hasta luego!")
                break
            else:
                print("\n❌ Opción inválida. Por favor selecciona 1-6.")

            input("\n📋 Presiona Enter para volver al menú principal...")

        except KeyboardInterrupt:
            print("\n\n👋 Saliendo...")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            input("Presiona Enter para continuar...")


if __name__ == "__main__":
    print("🚀 Iniciando sistema de demostración...")

    # Verificar archivos necesarios
    archivos_requeridos = [
        "codigo_vulnerable_demo.py", "analizar_codigo_vulnerable.py",
        "demo_vulnerabilities.py", "scripts/extract_features_from_diff.py",
        "scripts/generate_basic_report.py"
    ]

    faltantes = [
        archivo for archivo in archivos_requeridos
        if not os.path.exists(archivo)
    ]

    if faltantes:
        print("⚠️ ADVERTENCIA: Archivos faltantes:")
        for archivo in faltantes:
            print(f"   • {archivo}")
        print("\nAlgunas funciones pueden no funcionar correctamente.")
        input("Presiona Enter para continuar de todos modos...")

    main()
