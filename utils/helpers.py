import os
import socket
import json
import random
import string
import requests

# Função para obter informações sobre o IP usando uma API pública
def get_ip_info(ip):
    """Retorna informações sobre o IP usando uma API pública."""
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Função para verificar se um IP é válido
def is_valid_ip(ip):
    """Verifica se o IP está no formato correto (ex: 192.168.1.1)"""
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True

# Função para gerar uma string aleatória
def generate_random_string(length=10):
    """Gera uma string aleatória de letras e números."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Função para salvar dados no formato JSON
def save_json_data(file_path, data):
    """Salva os dados no formato JSON em um arquivo."""
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Dados salvos em {file_path}")

# Função para ler dados do formato JSON
def read_json_data(file_path):
    """Lê os dados de um arquivo JSON."""
    if not os.path.exists(file_path):
        print(f"Arquivo {file_path} não encontrado!")
        return None
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

# Função para obter o nome do host a partir de um IP
def get_hostname_from_ip(ip):
    """Obtém o nome do host a partir de um IP. Retorna 'N/A' caso não consiga resolver."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return 'N/A'

# Função para gerar um log simples de dados
def log_event(message):
    """Registra uma mensagem simples de log no console."""
    print(f"[{generate_random_string(5)}] {message}")

# Função para gerar um arquivo aleatório com conteúdo
def generate_random_file(file_name, file_size_kb=10):
    """Gera um arquivo aleatório de tamanho especificado (em KB)."""
    file_path = os.path.join("honeynet/fake_files", file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(os.urandom(file_size_kb * 1024))  # Escreve conteúdo aleatório no arquivo
    print(f"Arquivo aleatório gerado: {file_path}")

# Função para gerar um relatório simples em texto
def generate_simple_report(report_name="relatorio_fake.txt"):
    """Gera um relatório simples com informações de sistema."""
    report_path = os.path.join("honeynet/fake_reports", report_name)
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w') as f:
        f.write(f"Relatório Gerado - {generate_random_string(5)}\n")
        f.write("Informações de sistema:\n")
        f.write(f"Host: {socket.gethostname()}\n")
        f.write(f"Endereço IP: {socket.gethostbyname(socket.gethostname())}\n")
        f.write(f"Data e Hora: {generate_random_string(8)}\n")
    print(f"Relatório gerado: {report_path}")

# Função para gerar um arquivo de configuração falso (por exemplo, JSON)
def generate_fake_config(config_name="fake_config.json"):
    """Gera um arquivo de configuração JSON com dados aleatórios."""
    config_data = {
        "version": "1.0",
        "settings": {
            "enabled": random.choice([True, False]),
            "max_connections": random.randint(50, 200),
            "timeout": random.randint(5, 30)
        },
        "info": f"Configuração gerada por {generate_random_string(4)}"
    }
    config_path = os.path.join("honeynet/fake_configs", config_name)
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    save_json_data(config_path, config_data)
    print(f"Arquivo de configuração gerado: {config_path}")
    
# Função para gerar um arquivo de texto com informações aleatórias
def generate_random_text_file(file_name="random_text.txt", num_lines=20):
    """Gera um arquivo de texto com um número especificado de linhas aleatórias."""
    file_path = os.path.join("honeynet/fake_texts", file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        for _ in range(num_lines):
            f.write(f"{generate_random_string(20)}\n")
    print(f"Arquivo de texto gerado: {file_path}")
    
# Função para gerar um arquivo de senha falso
def generate_fake_password_file(file_name="fake_passwords.txt"):
    """Gera um arquivo de senhas falsas com padrões aleatórios."""
    file_path = os.path.join("honeynet/fake_passwords", file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        for _ in range(10):
            password = generate_random_string(12)
            f.write(f"{password}\n")
    print(f"Arquivo de senhas gerado: {file_path}")

# Função para gerar um conjunto completo de arquivos falsos
def generate_fake_documents(num_files=5):
    """Gera uma coleção completa de arquivos falsos como parte da honeynet."""
    log_event("Iniciando geração de arquivos falsos...")

    # Gera um número configurável de arquivos
    for _ in range(num_files):
        generate_random_file(f"fake_file_{generate_random_string(5)}.bin", random.randint(5, 20))
        generate_simple_report(f"relatorio_{generate_random_string(5)}.txt")
        generate_fake_config(f"config_{generate_random_string(5)}.json")
        generate_random_text_file(f"sample_text_{generate_random_string(5)}.txt", random.randint(10, 30))
        generate_fake_password_file(f"passwords_{generate_random_string(5)}.txt")

# Teste das funções
if __name__ == "__main__":
    # Testando funções de utilidades gerais
    log_event("Iniciando o sistema de honeynet")
    is_valid = is_valid_ip("192.168.1.1")
    print(f"IP válido? {is_valid}")
    
    # Gerando 5 arquivos falsos por padrão
    generate_fake_documents(num_files=5)
