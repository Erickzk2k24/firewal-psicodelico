import socket
import random
import time
from datetime import datetime
import requests

# Funções para detectar padrões de ataques
def detect_port_scan(ip):
    # Exemplo simples: verifica se há um grande número de tentativas de conexão em um curto período
    print(f"Detectando escaneamento de portas do IP: {ip}")
    return random.choice([True, False])  # Simula a detecção (True se ataque, False caso contrário)

def detect_sql_injection(request):
    # Exemplo de detecção de SQL Injection em uma URL
    if "' OR '1'='1" in request:
        print(f"Detectado SQL Injection na URL: {request}")
        return True
    return False

def detect_malicious_script(command):
    # Exemplo de detecção de execução de script malicioso
    malicious_keywords = ["malicioso.py", "reverse_shell", "nmap"]
    for keyword in malicious_keywords:
        if keyword in command:
            print(f"Comando malicioso detectado: {command}")
            return True
    return False

# Função para acionar a honeynet (simulada)
def trigger_honeynet(ip):
    print(f"Atacante {ip} direcionado para a honeynet!")
    # Aqui você poderia iniciar a honeynet real, como iniciar o servidor SSH falso, etc.
    # Vamos enviar o IP para o Flask (exemplo)
    response = requests.get(f'http://127.0.0.1:5000/block_attacker/{ip}')
    return response.json()

# Função para registrar um log do ataque
def log_attack(ip, action, command):
    log_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": ip,
        "action": action,
        "command": command,
    }
    # Aqui você poderia salvar os logs em um banco de dados (MongoDB, por exemplo)
    # Ou simplesmente enviar para o Flask para que a página seja atualizada
    print(f"Log registrado: {log_entry}")
    requests.post("http://127.0.0.1:5000/get_logs", json=log_entry)

# Função principal de detecção que centraliza as verificações de ataques
def detect_attack(ip, request=None, command=None):
    attack_data = {
        "ip": ip,
        "detected_attacks": []
    }

    # Verificar escaneamento de portas
    if detect_port_scan(ip):
        attack_data["detected_attacks"].append("Escaneamento de Portas")

    # Verificar SQL Injection
    if request and detect_sql_injection(request):
        attack_data["detected_attacks"].append("SQL Injection")

    # Verificar execução de script malicioso
    if command and detect_malicious_script(command):
        attack_data["detected_attacks"].append("Execução de Script Malicioso")

    return attack_data

# Função principal de monitoramento de rede
def monitor_network():
    while True:
        # Simulação de monitoramento de IPs de atacantes
        ip = f"192.168.1.{random.randint(1, 100)}"
        action = "Escaneamento de Portas"
        command = "nmap -sS"
        
        # Detecta o ataque
        attack_data = detect_attack(ip, command=command)
        if attack_data["detected_attacks"]:
            log_attack(ip, action, command)
            trigger_honeynet(ip)

        action = "Tentativa de SQL Injection"
        request = "GET /login' OR '1'='1"
        
        # Detecta SQL Injection
        attack_data = detect_attack(ip, request=request)
        if attack_data["detected_attacks"]:
            log_attack(ip, action, request)
            trigger_honeynet(ip)

        action = "Execução de Script Malicioso"
        command = "python3 malicioso.py"
        
        # Detecta execução de script malicioso
        attack_data = detect_attack(ip, command=command)
        if attack_data["detected_attacks"]:
            log_attack(ip, action, command)
            trigger_honeynet(ip)

        time.sleep(5)  # Simula monitoramento contínuo a cada 5 segundos

if __name__ == "__main__":
    monitor_network()
