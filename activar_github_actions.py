#!/usr/bin/env python3
"""
Script para hacer commit de código vulnerable y activar GitHub Actions
"""

import os
import subprocess
import time


def crear_commit_vulnerable():
    """Crea un commit con código vulnerable para activar GitHub Actions"""

    print("🚨 CREANDO COMMIT CON CÓDIGO VULNERABLE")
    print("=" * 50)

    # Verificar que el archivo vulnerable existe
    if not os.path.exists("codigo_vulnerable_demo.py"):
        print("❌ Error: No se encuentra codigo_vulnerable_demo.py")
        return False

    print("📄 Archivo vulnerable encontrado: codigo_vulnerable_demo.py")

    # Agregar el archivo al staging area
    try:
        print("📋 Agregando archivo al staging area...")
        subprocess.run(["git", "add", "codigo_vulnerable_demo.py"], check=True)

        # Crear mensaje de commit detallado
        mensaje_commit = """feat: Agregar código de prueba con vulnerabilidades críticas

🚨 ARCHIVO DE TESTING: codigo_vulnerable_demo.py

Este commit contiene intencionalmente múltiples vulnerabilidades:
- SQL Injection patterns (SELECT, WHERE, concatenación insegura)
- XSS vulnerabilities (innerHTML, alert, eval)  
- Command injection (os.system, subprocess)
- Funciones peligrosas (strcpy, gets, sprintf)
- Concatenación insegura de strings

🎯 DETECCIÓN ESPERADA:
- Score de riesgo: 142 (CRÍTICO)
- Patrones SQL: 1
- Patrones XSS: 10  
- Concatenaciones inseguras: 26
- Funciones peligrosas: 10
- Patrones inyección: 2

El sistema debería generar ALERTA CRÍTICA (>70% probabilidad)."""

        print("💾 Creando commit...")
        subprocess.run(["git", "commit", "-m", mensaje_commit], check=True)

        print("✅ Commit creado exitosamente!")

        # Push al repositorio para activar GitHub Actions
        print("🚀 Subiendo cambios al repositorio...")
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print("✅ Cambios subidos exitosamente!")
        print("\n" + "=" * 50)
        print("🎉 GITHUB ACTIONS SE ACTIVARÁ AUTOMÁTICAMENTE")
        print("=" * 50)

        print("🔍 El workflow debería:")
        print("   1. Detectar el archivo codigo_vulnerable_demo.py")
        print("   2. Extraer características avanzadas")
        print("   3. Analizar con modelo Random Forest")
        print("   4. Generar reporte HTML con alertas")
        print("   5. Crear artefactos con resultados")

        print(f"\n📊 RESULTADOS ESPERADOS:")
        print("   🚨 ALERTA CRÍTICA: >95% probabilidad vulnerabilidad")
        print("   📋 142 puntos de riesgo detectados")
        print("   ⚠️ Múltiples patrones críticos identificados")

        print(f"\n🌐 Puedes ver el progreso en:")
        print(
            "   https://github.com/4l3x1s456/SoftwareSeguro_MiniProyecto/actions"
        )

        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando Git: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False


def main():
    """Función principal"""

    print("🔒 ACTIVADOR DE GITHUB ACTIONS - DETECCIÓN DE VULNERABILIDADES")
    print("=" * 70)

    # Mostrar estado actual
    print("📋 Estado actual del repositorio:")
    try:
        result = subprocess.run(["git", "status", "--porcelain"],
                                capture_output=True,
                                text=True,
                                check=True)
        if result.stdout.strip():
            print("📄 Archivos modificados:")
            print(result.stdout)
        else:
            print("✅ Repositorio limpio, listo para crear commit")
    except:
        print("⚠️ No se pudo verificar el estado de Git")

    # Confirmar antes de proceder
    print(f"\n🤔 ¿Quieres crear un commit con código vulnerable?")
    print("   Esto activará GitHub Actions automáticamente.")

    respuesta = input("   Escribe 'si' para continuar: ").lower().strip()

    if respuesta in ['si', 'sí', 'yes', 'y']:
        if crear_commit_vulnerable():
            print("\n🎯 SIGUIENTE PASO:")
            print(
                "   Ve a GitHub Actions para ver la detección en tiempo real:")
            print(
                "   https://github.com/4l3x1s456/SoftwareSeguro_MiniProyecto/actions"
            )
        else:
            print("\n❌ Falló la creación del commit")
    else:
        print("\n👋 Operación cancelada")


if __name__ == "__main__":
    main()
