#!/usr/bin/env python3
"""
Script para extraer características del archivo de vulnerabilidades demo
Genera example_features.csv para que el modelo C++ pueda analizarlo
"""

import pandas as pd
import os


def extract_features_from_demo_file():
    """Extrae características del archivo codigo_vulnerable_demo.py"""

    # Leer el archivo de vulnerabilidades
    demo_file = "codigo_vulnerable_demo.py"

    if not os.path.exists(demo_file):
        print(f"❌ Error: No se encuentra el archivo {demo_file}")
        return None

    with open(demo_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extraer características usando la misma funcion que en preprocesar_vulnerabilidades.py
    features = extract_code_features(content)

    # Agregar score promedio como en entrenamiento
    mean_score = 5.52572202166065

    # Crear array de características en el orden correcto
    feature_array = [
        features['len'], features['num_lines'], features['num_semi'],
        features['num_if'], features['num_for'], features['num_while'],
        features['num_equal'], features['sql_risk'], features['xss_risk'],
        features['concat_risk'], features['dangerous_count'],
        features['injection_risk'], mean_score
    ]

    # Guardar en example_features.csv para el modelo C++
    df = pd.DataFrame([feature_array])
    df.to_csv("example_features.csv", index=False, header=False)

    # Mostrar análisis detallado
    print("🔍 ANÁLISIS DEL CODIGO VULNERABLE:")
    print("=" * 50)
    print(f"📄 Archivo analizado: {demo_file}")
    print(f"📊 Características extraídas:")
    print(f"   • Longitud total: {features['len']} caracteres")
    print(f"   • Número de líneas: {features['num_lines']}")
    print(f"   • Patrones SQL detectados: {features['sql_risk']}")
    print(f"   • Patrones XSS detectados: {features['xss_risk']}")
    print(f"   • Concatenaciones inseguras: {features['concat_risk']}")
    print(f"   • Funciones peligrosas: {features['dangerous_count']}")
    print(f"   • Patrones de inyeccion: {features['injection_risk']}")

    # Calcular score de riesgo
    risk_score = (features['sql_risk'] * 2) + (features['xss_risk'] * 2) + \
                 (features['concat_risk'] * 3) + (features['dangerous_count'] * 4) + \
                 features['injection_risk']

    print(f"\n🎯 SCORE DE RIESGO CALCULADO: {risk_score}")

    if risk_score > 20:
        print("🚨 NIVEL DE RIESGO: CRÍTICO")
    elif risk_score > 10:
        print("⚠️ NIVEL DE RIESGO: ALTO")
    elif risk_score > 5:
        print("🟡 NIVEL DE RIESGO: MEDIO")
    else:
        print("✅ NIVEL DE RIESGO: BAJO")

    print(f"\n✅ Características guardadas en example_features.csv")
    print(
        "   Ahora puedes usar el modelo C++ (Opcion 2) para analizar este codigo"
    )

    return feature_array


def extract_code_features(code_text):
    """Extrae características del codigo usando la misma logica que preprocesar_vulnerabilidades.py"""
    text = str(code_text).lower()

    # Características básicas
    length = len(text)
    num_lines = text.count("\n") + 1
    num_semi = text.count(";")
    num_if = text.count("if")
    num_for = text.count("for")
    num_while = text.count("while")
    num_equal = text.count("=")

    # Patrones de riesgo específicos para vulnerabilidades
    # SQL Injection patterns
    sql_patterns = [
        "select", "insert", "update", "delete", "union", "drop", "alter"
    ]
    sql_risk = sum([text.count(pattern) for pattern in sql_patterns])

    # XSS patterns
    xss_patterns = [
        "alert", "document", "innerhtml", "script", "eval", "settimeout"
    ]
    xss_risk = sum([text.count(pattern) for pattern in xss_patterns])

    # Concatenacion insegura (patron común en ambas vulnerabilidades)
    concat_risk = text.count("' +") + text.count('" +') + text.count(
        "+ '") + text.count('+ "')

    # Funciones deprecated o peligrosas
    dangerous_funcs = ["gets", "strcpy", "sprintf", "strcat", "system", "exec"]
    dangerous_count = sum([text.count(func) for func in dangerous_funcs])

    # Patrones de inyeccion
    injection_patterns = ["where", "from", "into", "values"]
    injection_risk = sum(
        [text.count(pattern) for pattern in injection_patterns])

    return {
        "len": length,
        "num_lines": num_lines,
        "num_semi": num_semi,
        "num_if": num_if,
        "num_for": num_for,
        "num_while": num_while,
        "num_equal": num_equal,
        "sql_risk": sql_risk,
        "xss_risk": xss_risk,
        "concat_risk": concat_risk,
        "dangerous_count": dangerous_count,
        "injection_risk": injection_risk
    }


def main():
    """Funcion principal"""
    print("🔍 EXTRACTOR DE CARACTERÍSTICAS - CODIGO VULNERABLE")
    print("Genera example_features.csv para análisis con modelo C++")
    print("=" * 60)

    result = extract_features_from_demo_file()

    if result:
        print("\n" + "=" * 60)
        print("✅ PROCESO COMPLETADO")
        print(
            "📋 Siguiente paso: Ejecutar ./Modelo_MineriaDatos.exe y seleccionar opcion 2"
        )
        return True
    else:
        print("❌ Error en el proceso")
        return False


if __name__ == "__main__":
    main()
