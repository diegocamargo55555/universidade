# Use a imagem base oficial do Ubuntu
FROM ubuntu:latest

# Evita que a instalação de pacotes peça interações manuais
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza os pacotes e instala o Go (Golang)
RUN apt-get update && \
    apt-get install -y golang-go

# Cria o diretório /T2 e o define como diretório de trabalho
WORKDIR /T2

# Copia o arquivo client.go para o diretório de trabalho (/T2) na imagem
COPY server.go .

EXPOSE 8080
