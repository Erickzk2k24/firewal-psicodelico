import subprocess

def create_fake_ftp_server():
    # Simula um servidor FTP com autenticação anônima
    ftp_config = """
    anonymous_enable=YES
    write_enable=YES
    """
    # Escreve a configuração no arquivo de configuração do FTP
    with open("/etc/vsftpd.conf", "w") as f:
        f.write(ftp_config)

    # Inicia um servidor FTP simulado
    subprocess.run(["service", "vsftpd", "start"])
    print("Servidor FTP falso iniciado!")
