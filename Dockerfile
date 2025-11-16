# Usa a imagem oficial do Python 3.11 como base
FROM python:3.11-slim

# Define a pasta de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de dependências (requirements.txt)
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da sua aplicação
COPY test_api.py .

# Comando de inicialização: Uvicorn rodando o app
# NOTA: Usamos $PORT para que o Railway injete a porta correta.
CMD uvicorn test_api:app --host 0.0.0.0 --port $PORT
