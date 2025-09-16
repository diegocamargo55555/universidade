package main

import (
	"fmt"
	"net"
	"os"
)

func main() {
	var conn net.Conn
	var err error

	//host := "172.31.71.2/18"
	conn, err = net.Dial("tcp", "172.31.71.2:8080")

	if err != nil {
		fmt.Printf("Não foi possível conectar ao servidor: %s\n", err)
		os.Exit(1)
	}
	defer conn.Close()

	fmt.Println("Conectado ao servidor Ubuntu!")
	_, err = conn.Write([]byte("Olá, servidor Ubuntu! Sou o cliente."))
	if err != nil {
		fmt.Printf("Erro ao enviar mensagem: %s\n", err)
		return
	}

	buf := make([]byte, 1024)
	n, err := conn.Read(buf)
	if err != nil {
		fmt.Printf("Erro ao ler resposta: %s\n", err)
		return
	}

	fmt.Printf("Resposta do servidor: %s\n", string(buf[:n]))
}
