import random
import string
import os
import json
import time

def random_string(length):
    """Gera uma string aleatória de letras e números"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_fake_log():
    """Gera um log falso do sistema com uma data aleatória"""
    log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(random.randint(1600000000, 1700000000))),
        "level": random.choice(["INFO", "WARN", "ERROR", "DEBUG"]),
        "message": f"Process {random_string(5)} started with status {random.choice(['success', 'failure'])}.",
        "user": f"user{random.randint(1, 10)}",
        "ip": f"192.168.1.{random.randint(1, 255)}"
    }
    return json.dumps(log)

def generate_fake_config():
    """Gera um arquivo de configuração falso com dados irreais"""
    config = {
        "host": f"192.168.1.{random.randint(1, 255)}",
        "port": random.randint(1000, 65535),
        "username": random_string(8),
        "password": random_string(12),
        "timeout": random.randint(30, 300)
    }
    return json.dumps(config, indent=4)

def generate_fake_script():
    """Gera um script falso (Python, Bash) com comportamento simulado"""
    script_type = random.choice(["python", "bash"])
    if script_type == "python":
        script = f"""
# Script falso - {random_string(5)}
import os
print('Esse é um script falso! Não faça nada!'
os.system('echo Fake Command Executed')
"""
    else:
        script = f"""
# Script falso - {random_string(5)}
echo "Esse é um script falso!" > /tmp/fake.log
"""
    return script

def create_fake_files():
    """Cria diretórios e arquivos com dados falsos"""
    fake_dir = "honeynet/generated_fake_files"
    os.makedirs(fake_dir, exist_ok=True)

    # Gerar arquivos falsos de diferentes tipos
    fake_files = [
        {"name": "fake_log.json", "content": generate_fake_log()},
        {"name": "fake_config.json", "content": generate_fake_config()},
        {"name": "fake_script.py", "content": generate_fake_script()},
        {"name": "fake_bash.sh", "content": generate_fake_script()}
    ]

    # Criar arquivos e escrever conteúdo
    for fake_file in fake_files:
        file_path = os.path.join(fake_dir, fake_file["name"])
        with open(file_path, "w") as f:
            f.write(fake_file["content"])
        print(f"Arquivo falso gerado: {file_path}")

create_fake_files()
