# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Instale as dependências do sistema, se necessário
# Exemplo: RUN apt-get update && apt-get install -y gcc

# Copie o arquivo de dependências para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências da aplicação
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação para o diretório de trabalho
COPY ./src /app/src
COPY ./setup.py /app/

# Instala o projeto em modo editável para que os módulos sejam encontrados
RUN pip install -e .

# Exponha a porta em que a aplicação irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação com Uvicorn
# O host 0.0.0.0 torna a aplicação acessível de fora do contêiner
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 