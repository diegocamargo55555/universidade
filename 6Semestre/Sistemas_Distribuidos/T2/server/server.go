package main

import (
	"fmt"
	"io"
	"net"
	"os"
)

func main() {
	port := "8080"
	listener, err := net.Listen("tcp", ":"+port)
	if err != nil {
		fmt.Printf("Erro ao iniciar o servidor: %s\n", err)
		os.Exit(1)
	}
	defer listener.Close()
	fmt.Printf("Servidor Ubuntu escutando na porta %s\n", port)

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Printf("Erro ao aceitar conexão: %s\n", err)
			continue
		}
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer conn.Close()
	fmt.Printf("Cliente conectado de: %s\n", conn.RemoteAddr().String())
	buf := make([]byte, 1024) 
	n, err := conn.Read(buf)
	if err != nil {
		if err != io.EOF {
			fmt.Printf("Erro ao ler dados do cliente: %s\n", err)
		}
		return
	}
	message := string(buf[:n])
	fmt.Printf("Mensagem recebida: %s\n", message)
	_, err = conn.Write([]byte("Mensagem recebida pelo servidor Ubuntu!"))
	if err != nil {
		fmt.Printf("Erro ao enviar resposta: %s\n", err)
	}
}
