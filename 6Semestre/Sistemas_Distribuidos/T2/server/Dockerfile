FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y golang-go

WORKDIR /T2

COPY server.go .

EXPOSE 8080
