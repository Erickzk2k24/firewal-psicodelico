from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from detector.detector import detect_attack
from logger.logger import log_attack_detection, log_fake_file_generation, log_action
from ia_generator.generate_fake_docs import create_fake_docs  # Correção para a função correta
from utils.helpers import get_ip_info


# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Rota principal - Dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Rota para detectar ataque e gerar arquivos falsos
@app.route('/detect', methods=['POST'])
def detect():
    attacker_ip = request.form.get('ip')  # O IP do atacante será enviado via POST

    if not attacker_ip:
        return jsonify({"error": "IP não fornecido"}), 400
    
    # Detectar o ataque
    attack_data = detect_attack(attacker_ip)

    if not attack_data or not attack_data.get("detected_attacks"):
        return jsonify({"error": "Não foi possível detectar o ataque"}), 500

    # Registrar ataque no MongoDB e também gerar logs
    log_attack_detection(attacker_ip, attack_data['detected_attacks'])

    # Gerar arquivos falsos com base no ataque detectado
    create_fake_docs()  # Correção: chamando a função correta para gerar arquivos

    # Listar arquivos gerados no diretório honeynet/fake_docs
    fake_files = os.listdir("honeynet/fake_docs")
    
    # Verificar se há arquivos falsos gerados
    if not fake_files:
        return jsonify({"error": "Nenhum arquivo falso gerado"}), 500
    
    for file in fake_files:
        log_fake_file_generation(file, "documento")  # Registrando a criação de cada arquivo

    # Log de ação executada (ex: bloqueio de IP, execução de algum comando)
    log_action("Bloqueio de IP", f"Bloqueio do IP {attacker_ip} após detectar ataque")

    return jsonify({
        "status": "success",
        "attack_data": attack_data,
        "fake_files": fake_files
    })

# Rota para buscar informações de IP e navegador
@app.route('/info', methods=['GET'])
def info():
    user_ip = request.remote_addr
    user_browser = request.user_agent.string
    
    # Obter informações de IP e navegador
    ip_info = get_ip_info(user_ip)
    browser_info = get_browser_info(user_browser)

    return jsonify({
        "ip_info": ip_info,
        "browser_info": browser_info
    })

if __name__ == '__main__':
    app.run(debug=True)
