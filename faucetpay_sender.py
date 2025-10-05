import requests
import time
import mysql.connector
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class FaucetPay:
    BASE = "https://faucetpay.io/api/v1/"
    
    def __init__(self, api_key):
        self.api_key = api_key

    def post_request(self, method, params=None):
        if params is None:
            params = {}
        params['api_key'] = self.api_key
        url = f"{self.BASE}{method}"
        response = requests.post(url, data=params)
        return response.json()

    def send_funds(self, currency, amount, email):
        params = {
            "currency": currency,
            "amount": amount,
            "to": email,
            "referral": 'true'
        }
        return self.post_request("send", params)

def conectar_banco_dados():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def buscar_emails_referencia_true():
    conn = conectar_banco_dados()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT DISTINCT(email_ttt) as email FROM `range_bonus_btc` WHERE fl_processada = 1")
    emails = cursor.fetchall()
    cursor.close()
    conn.close()
    return [email['email'] for email in emails]

def enviar_fundos(api_key, email, moeda, valor):
    faucetpay = FaucetPay(api_key)
    response = faucetpay.send_funds(moeda, valor, email)
    print(f"Enviando {valor} {moeda} para {email}: {response.get('message', 'Erro desconhecido')}")
    return response

if __name__ == "__main__":
    # Carrega configurações das variáveis de ambiente
    api_key = os.getenv("FAUCETPAY_API_KEY")
    moeda_a_enviar = os.getenv("CURRENCY", "BTC")
    valor_a_enviar = float(os.getenv("AMOUNT", "2"))
    intervalo_segundos = int(os.getenv("DELAY_SECONDS", "2"))
    
    if not api_key:
        raise ValueError("FAUCETPAY_API_KEY não configurada no arquivo .env")
    
    emails = buscar_emails_referencia_true()
    print(f"Total de emails a processar: {len(emails)}")
    
    for email in emails:
        print(f"Processando envio para: {email}")
        enviar_fundos(api_key, email, moeda_a_enviar, valor_a_enviar)
        time.sleep(intervalo_segundos)