import random
import string
import os
import json
import time

def random_string(length):
    """Gera uma string aleatória de letras e números"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_fake_report():
    """Gera um relatório falso (por exemplo, relatório de sistema ou de auditoria)"""
    report = f"""
    Relatório de Auditoria - {random_string(5)}
    Data: {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(random.randint(1600000000, 1700000000)))}
    
    Atividade do Sistema:
    ------------------------
    - Processo: {random_string(6)}
    - Status: {random.choice(['Concluído', 'Em andamento', 'Falhou'])}
    - Usuário: {random_string(4)}
    - IP de Acesso: 192.168.1.{random.randint(1, 255)}
    
    Ações:
    - Ação 1: {random.choice(['Iniciado', 'Abortado', 'Finalizado'])}
    - Ação 2: {random.choice(['Sucesso', 'Falha', 'Aviso'])}
    
    Observações:
    - {random_string(10)}
    
    Conclusão:
    - Ação recomendada: {random.choice(['Revisar Configuração', 'Ignorar', 'Aguardar'])}
    """
    return report

def generate_fake_contract():
    """Gera um contrato falso, como um contrato de software ou de licença"""
    contract = f"""
    CONTRATO DE LICENÇA DE SOFTWARE - {random_string(5)}
    Data: {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(random.randint(1600000000, 1700000000)))}
    
    CLÁUSULA 1 - OBJETO
    A empresa {random_string(6)} concede ao usuário o direito de utilizar o software {random_string(4)} nas condições aqui estabelecidas.
    
    CLÁUSULA 2 - VIGÊNCIA
    O presente contrato entra em vigor na data de sua assinatura e permanecerá válido por {random.randint(1, 10)} anos.
    
    CLÁUSULA 3 - OBRIGAÇÕES
    O usuário compromete-se a não modificar, distribuir ou vender o software.
    
    CLÁUSULA 4 - RESCISÃO
    O contrato poderá ser rescindido a qualquer momento, mediante violação dos termos aqui descritos.
    
    ASSINATURA:
    _______________________
    Empresa: {random_string(6)}
    Usuário: {random_string(6)}
    """
    return contract

def generate_fake_log():
    """Gera um log falso do sistema em formato JSON"""
    log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(random.randint(1600000000, 1700000000))),
        "level": random.choice(["INFO", "WARN", "ERROR", "DEBUG"]),
        "message": f"Processo {random_string(5)} iniciado com status {random.choice(['sucesso', 'falha'])}.",
        "user": f"user{random.randint(1, 10)}",
        "ip": f"192.168.1.{random.randint(1, 255)}"
    }
    return json.dumps(log)

def generate_fake_script():
    """Gera um script falso em Python ou Bash"""
    script_type = random.choice(["python", "bash"])
    if script_type == "python":
        script = f"""
# Script falso - {random_string(5)}
import os
print('Este é um script falso!')
os.system('echo Comando falso executado')
"""
    else:
        script = f"""
# Script falso - {random_string(5)}
echo "Este é um script falso!" > /tmp/fake.log
"""
    return script

def create_fake_docs():
    """Cria diretórios e documentos falsos em vários formatos"""
    fake_dir = "honeynet/fake_docs"
    os.makedirs(fake_dir, exist_ok=True)  # Garantir que o diretório será criado

    # Gerar documentos falsos de diferentes tipos
    fake_docs = [
        {"name": "fake_report.txt", "content": generate_fake_report()},
        {"name": "fake_contract.txt", "content": generate_fake_contract()},
        {"name": "fake_log.json", "content": generate_fake_log()},
        {"name": "fake_script.py", "content": generate_fake_script()},
        {"name": "fake_bash.sh", "content": generate_fake_script()}
    ]

    # Criar arquivos e escrever conteúdo
    for fake_doc in fake_docs:
        file_path = os.path.join(fake_dir, fake_doc["name"])
        with open(file_path, "w") as f:
            f.write(fake_doc["content"])
        print(f"Documento falso gerado: {file_path}")

# Executando a criação dos documentos falsos
create_fake_docs()
