import logging
import os
import json
from datetime import datetime

# Definindo o diretório para armazenar os logs
log_dir = "honeynet/logs"
os.makedirs(log_dir, exist_ok=True)

# Configuração básica do logger
log_file = os.path.join(log_dir, "honeynet_logs.log")
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event_type, event_data):
    """
    Função para registrar eventos importantes no sistema.
    :param event_type: Tipo do evento (ex: 'Ataque Detectado', 'Arquivo Falso Gerado').
    :param event_data: Dados adicionais sobre o evento (ex: IP do atacante, tipo de arquivo gerado).
    """
    event_message = f"Evento: {event_type} | Dados: {json.dumps(event_data)}"
    logging.info(event_message)

def log_attack_detection(ip, attack_type):
    """
    Função para logar a detecção de um ataque.
    :param ip: IP do atacante detectado.
    :param attack_type: Tipo de ataque detectado (ex: 'Exploração de Vulnerabilidade', 'Ataque DDoS').
    """
    event_data = {
        "ip": ip,
        "attack_type": attack_type,
        "status": "detectado"
    }
    log_event("Ataque Detectado", event_data)

def log_fake_file_generation(file_name, file_type):
    """
    Função para logar a geração de arquivos falsos.
    :param file_name: Nome do arquivo gerado.
    :param file_type: Tipo do arquivo (ex: 'script', 'log', 'documento').
    """
    event_data = {
        "file_name": file_name,
        "file_type": file_type,
        "status": "gerado"
    }
    log_event("Arquivo Falso Gerado", event_data)

def log_action(action, details):
    """
    Função para logar ações realizadas pelo sistema.
    :param action: Ação executada (ex: 'Bloqueio de IP', 'Execução de Script').
    :param details: Detalhes sobre a ação executada.
    """
    event_data = {
        "action": action,
        "details": details,
        "status": "executado"
    }
    log_event("Ação Executada", event_data)

# Teste das funções de log
if __name__ == "__main__":
    # Log de detecção de ataque
    log_attack_detection("192.168.1.101", "Exploração de Vulnerabilidade")
    
    # Log de geração de arquivo falso
    log_fake_file_generation("fake_log.json", "log")
    
    # Log de ação executada
    log_action("Bloqueio de IP", "Bloqueio do IP 192.168.1.101 após detectar ataque")
    
    print("Logs gerados com sucesso!")
