# 🚨 ARCHIVO DE DEMO: Contiene vulnerabilidades intencionalmente para testing

import os
import subprocess


def vulnerable_sql_example():
    """
    Función con SQL Injection crítico
    Debería generar ALERTA MÁXIMA
    """
    username = input("Enter username: ")
    password = input("Enter password: ")

    # VULNERABLE: Concatenación directa (patrón crítico)
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

    # PELIGROSO: system() con input del usuario
    os.system("mysql -h localhost -u root -p -e \"" + query + "\"")

    return query


def xss_vulnerability_example():
    """
    XSS con múltiples vectores de ataque
    """
    user_input = input("Enter your message: ")

    # VULNERABLE: innerHTML sin escapar
    html_output = "<div>User said: " + user_input + "</div>"

    # CRÍTICO: eval() con contenido del usuario
    javascript = "document.innerHTML = '" + html_output + "'; alert('XSS executed');"

    return "<script>" + javascript + "</script>"


def buffer_overflow_simulation():
    """
    Simulación de funciones peligrosas de C
    """
    data = input("Enter buffer data: ")

    # Simular funciones inseguras
    dangerous_ops = [
        "strcpy(buffer, '" + data + "');",
        "sprintf(output, '%s', '" + data + "');", "gets(" + data + ");",
        "strcat(dest, '" + data + "');"
    ]

    return " ".join(dangerous_ops)


def command_injection_critical():
    """
    Inyección de comandos crítica
    """
    filename = input("Enter filename: ")

    # CRÍTICO: Múltiples vectores de command injection
    commands = [
        "system('cat " + filename + "')", "exec('rm -rf " + filename + "')",
        "subprocess.call('ls " + filename + "', shell=True)"
    ]

    for cmd in commands:
        print(f"Executing: {cmd}")

    return commands
