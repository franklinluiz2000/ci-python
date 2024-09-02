# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos necessários para o diretório de trabalho
COPY main.py .
COPY test_main.py .
COPY requirements.txt .

# Instala as dependências do Python listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para rodar os testes com pytest
CMD ["pytest", "test_main.py"]
