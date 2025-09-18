package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

func main() {
	var conn net.Conn
	var err error

	fmt.Print("Digite seu nome de usuário: ")
	reader := bufio.NewReader(os.Stdin)
	username, _ := reader.ReadString('\n')
	username = strings.TrimSpace(username)

	
	conn, err = net.Dial("tcp", "servidor:8080")
	if err != nil {
		fmt.Printf("Não foi possível conectar ao servidor: %s\n", err)
		os.Exit(1)
	}
	defer conn.Close()

	_, err = conn.Write([]byte(username))
	if err != nil {
		fmt.Printf("Erro ao enviar o nome de usuário: %s\n", err)
		return
	}

	fmt.Printf("Conectado como '%s' ao servidor\n", username)

	go func() { // ler oq o servidor envia
		buf := make([]byte, 1024)
		for {
			n, err := conn.Read(buf)
			if err != nil {
				fmt.Printf("Erro ao ler resposta do servidor: %s\n", err)
				return
			}
			fmt.Print(string(buf[:n]))
		}
	}()

	scanner := bufio.NewScanner(os.Stdin) // envia msg
	for scanner.Scan() {
		message := scanner.Text()
		_, err := conn.Write([]byte(message))
		if err != nil {
			fmt.Printf("Erro ao enviar mensagem: %s\n", err)
			return
		}
	}
}
