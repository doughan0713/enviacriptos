# 💰 FaucetPay Automated Sender

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

Sistema profissional para automação de envios em massa de criptomoedas através da API do FaucetPay, com integração a banco de dados MySQL.

[Características](#-características) •
[Instalação](#-instalação) •
[Configuração](#%EF%B8%8F-configuração) •
[Uso](#-uso) •
[API](#-api-reference) •
[FAQ](#-faq)

</div>

---

## 📖 Sobre o Projeto

O **FaucetPay Automated Sender** é uma solução robusta e escalável para enviar criptomoedas automaticamente para múltiplos destinatários. Ideal para:

- 🎁 Programas de bônus e recompensas
- 💸 Pagamentos em massa automatizados
- 🔄 Distribuição de comissões de referência
- 📊 Gestão de carteiras de múltiplos usuários

## ✨ Características

- ⚡ **Alta Performance**: Processamento rápido com controle de taxa
- 🔒 **Seguro**: Credenciais protegidas via variáveis de ambiente
- 📊 **Logging Detalhado**: Rastreamento completo de todas as transações
- 🗄️ **Integração MySQL**: Consultas otimizadas ao banco de dados
- 🔄 **Retry Logic**: Tratamento inteligente de erros
- 🌐 **Multi-moeda**: Suporte a todas as criptomoedas do FaucetPay
- 📈 **Escalável**: Processa centenas de transações eficientemente

## 🚀 Tecnologias

- **Python 3.7+**: Linguagem principal
- **Requests**: Cliente HTTP para API
- **MySQL Connector**: Integração com banco de dados
- **Python-dotenv**: Gerenciamento de variáveis de ambiente

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

- Python 3.7 ou superior instalado
- MySQL Server 5.7+ ou MariaDB 10.2+
- Conta ativa no [FaucetPay](https://faucetpay.io)
- API Key do FaucetPay
- Git (opcional)

## 🔧 Instalação

### Método 1: Clone via Git

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/faucetpay-sender.git

# Entre no diretório
cd faucetpay-sender

# Crie um ambiente virtual (recomendado)
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Método 2: Instalação Manual

```bash
# Crie o diretório do projeto
mkdir faucetpay-sender && cd faucetpay-sender

# Instale as dependências
pip install requests mysql-connector-python python-dotenv
```

## ⚙️ Configuração

### 1. Estrutura do Banco de Dados

Execute o seguinte SQL no seu MySQL:

```sql
CREATE DATABASE IF NOT EXISTS spam;
USE spam;

CREATE TABLE IF NOT EXISTS range_bonus_btc (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email_ttt VARCHAR(255) NOT NULL,
    fl_processada TINYINT(1) DEFAULT 0,
    valor_bonus DECIMAL(16,8) DEFAULT 0,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_processamento TIMESTAMP NULL,
    INDEX idx_fl_processada (fl_processada),
    INDEX idx_email (email_ttt)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### 2. Arquivo de Configuração

Crie o arquivo `.env` na raiz do projeto:

```env
# ============================================
# FAUCETPAY API CONFIGURATION
# ============================================
FAUCETPAY_API_KEY=sua_api_key_aqui

# ============================================
# SENDING CONFIGURATION
# ============================================
CURRENCY=BTC
AMOUNT=2
DELAY_SECONDS=2

# ============================================
# DATABASE CONFIGURATION
# ============================================
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=seu_usuario
DB_PASSWORD=sua_senha_segura
DB_NAME=spam

# ============================================
# ADVANCED SETTINGS (Optional)
# ============================================
# MAX_RETRIES=3
# TIMEOUT_SECONDS=30
# LOG_LEVEL=INFO
```

### 3. Obter API Key do FaucetPay

1. Acesse [FaucetPay Dashboard](https://faucetpay.io/dashboard)
2. Vá em **Settings** → **API**
3. Clique em **Generate New API Key**
4. Copie a chave e cole no arquivo `.env`

## 🎯 Uso

### Uso Básico

```bash
python faucetpay_sender.py
```

### Exemplo de Output

```
Total de emails a processar: 150
Processando envio para: user1@example.com
Enviando 2 BTC para user1@example.com: Payment sent successfully
Processando envio para: user2@example.com
Enviando 2 BTC para user2@example.com: Payment sent successfully
...
```

### Uso Avançado

```python
from faucetpay_sender import FaucetPay, enviar_fundos

# Criar instância personalizada
api = FaucetPay("sua_api_key")

# Enviar para email específico
response = api.send_funds(
    currency="DOGE",
    amount=100,
    email="usuario@exemplo.com"
)

print(response)
```

## 📚 API Reference

### Classe FaucetPay

```python
class FaucetPay:
    def __init__(self, api_key: str)
    def post_request(self, method: str, params: dict = None) -> dict
    def send_funds(self, currency: str, amount: float, email: str) -> dict
```

#### Métodos

**`send_funds(currency, amount, email)`**

Envia fundos para um destinatário.

**Parâmetros:**
- `currency` (str): Código da criptomoeda (BTC, ETH, DOGE, etc.)
- `amount` (float): Quantidade a enviar
- `email` (str): Email do destinatário registrado no FaucetPay

**Retorna:**
- `dict`: Resposta da API com status e mensagem

**Exemplo:**
```python
response = faucetpay.send_funds("BTC", 0.00001, "user@example.com")
```

### Funções Auxiliares

**`conectar_banco_dados()`**

Estabelece conexão com o MySQL usando credenciais do `.env`.

**`buscar_emails_referencia_true()`**

Retorna lista de emails com `fl_processada = 1`.

**`enviar_fundos(api_key, email, moeda, valor)`**

Wrapper simplificado para envio de fundos.

## 💰 Moedas Suportadas

| Símbolo | Nome | Valor Mínimo |
|---------|------|--------------|
| BTC | Bitcoin | 0.00000001 |
| ETH | Ethereum | 0.000001 |
| LTC | Litecoin | 0.00001 |
| DOGE | Dogecoin | 0.1 |
| BCH | Bitcoin Cash | 0.00001 |
| DASH | Dash | 0.00001 |
| TRX | Tron | 0.01 |
| USDT | Tether | 0.001 |
| BNB | Binance Coin | 0.0001 |
| USDC | USD Coin | 0.001 |

*Para lista completa, consulte a [documentação oficial do FaucetPay](https://faucetpay.io/page/api).*

## 📊 Estrutura do Projeto

```
faucetpay-sender/
│
├── faucetpay_sender.py    # Script principal
├── .env                    # Configurações (não versionar)
├── .env.example           # Exemplo de configuração
├── requirements.txt       # Dependências Python
├── README.md             # Documentação
├── .gitignore            # Arquivos ignorados
│
├── logs/                  # Logs de execução (opcional)
│   └── transactions.log
│
└── tests/                 # Testes unitários (opcional)
    └── test_faucetpay.py
```

## 🔒 Segurança

### Boas Práticas

✅ **FAZER:**
- Usar variáveis de ambiente para credenciais
- Manter `.env` no `.gitignore`
- Usar HTTPS para todas as requisições
- Implementar rate limiting
- Fazer backup regular do banco de dados
- Validar emails antes de enviar
- Monitorar logs de transações

❌ **NÃO FAZER:**
- Commitar credenciais no código
- Compartilhar sua API Key
- Desabilitar SSL/TLS
- Enviar valores sem validação
- Ignorar erros da API

### .gitignore Recomendado

```gitignore
# Environment variables
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log
logs/

# Database
*.sql
*.db
*.sqlite
```

## 🐛 Troubleshooting

### Erro: "Invalid API Key"

**Solução:**
```bash
# Verifique se a API Key está correta
echo $FAUCETPAY_API_KEY

# Gere uma nova no painel do FaucetPay
```

### Erro: "Insufficient Balance"

**Solução:**
- Verifique o saldo na sua conta FaucetPay
- Certifique-se de ter fundos suficientes para cobrir todas as transações + taxas

### Erro: "Connection refused (MySQL)"

**Solução:**
```bash
# Verifique se o MySQL está rodando
sudo systemctl status mysql

# Teste a conexão
mysql -h 127.0.0.1 -u seu_usuario -p
```

### Erro: "Rate Limit Exceeded"

**Solução:**
```env
# Aumente o delay no .env
DELAY_SECONDS=5
```

## 📈 Performance

### Benchmarks

| Transações | Tempo Médio | Delay |
|-----------|-------------|-------|
| 10 | 25s | 2s |
| 50 | 2m 10s | 2s |
| 100 | 4m 20s | 2s |
| 500 | 21m 40s | 2s |

### Otimizações

1. **Conexão Persistente**: Mantém conexão MySQL aberta
2. **Batch Processing**: Processa em lotes quando possível
3. **Async IO**: Considere usar `asyncio` para grandes volumes
4. **Caching**: Cache de emails já processados

## 🧪 Testes

```bash
# Instalar dependências de teste
pip install pytest pytest-cov

# Executar testes
pytest tests/

# Com cobertura
pytest --cov=faucetpay_sender tests/
```

## 🤝 Contribuindo

Contribuições são muito bem-vindas! 

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Changelog

### v1.0.0 (2025-10-05)
- ✨ Release inicial
- 🔒 Implementação de segurança com .env
- 📊 Sistema de logging
- 🗄️ Integração com MySQL
- 🌐 Suporte multi-moeda

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 💬 FAQ

**Q: Qual o limite de envios por dia?**  
A: Depende do seu plano no FaucetPay. Consulte a documentação oficial.

**Q: Posso usar com outras APIs de criptomoedas?**  
A: Este projeto é específico para FaucetPay, mas pode ser adaptado.

**Q: Como faço backup dos dados?**  
A: Use `mysqldump` para backup regular do banco de dados.

**Q: É seguro armazenar API Keys?**  
A: Sim, desde que use `.env` e nunca commite este arquivo.

**Q: Funciona com Python 2.7?**  
A: Não, requer Python 3.7 ou superior.

## 📧 Suporte

- 📖 [Documentação FaucetPay](https://faucetpay.io/page/api)
- 💬 [Issues no GitHub](https://github.com/seu-usuario/faucetpay-sender/issues)
- 📮 Email: contato@softpog.com.br

## 🙏 Agradecimentos

- [FaucetPay](https://faucetpay.io/?r=3122571) pela excelente API
- Comunidade Python pelo suporte
- Todos os contribuidores do projeto

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

Feito com ❤️ e ☕ por [Seu Nome](https://github.com/doughanmoraes)

</div># enviacriptos
