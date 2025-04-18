import subprocess

def create_fake_ssh_server():
    # Simula um servidor SSH com uma configuração vulnerável
    ssh_config = """
    PermitRootLogin yes
    PasswordAuthentication yes
    """
    # Escreve a configuração em um arquivo de configuração do SSH
    with open("/etc/ssh/sshd_config", "w") as f:
        f.write(ssh_config)

    # Inicia um servidor SSH simulado
    subprocess.run(["service", "ssh", "start"])
    print("Servidor SSH falso iniciado!")
