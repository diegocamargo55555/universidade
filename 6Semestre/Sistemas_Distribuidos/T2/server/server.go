package main

import (
	"fmt"
	"io"
	"net"
	"os"
	"strings"
	"sync"
)

type client struct {
	conn     net.Conn
	username string
}

var wg sync.WaitGroup
var messages = make(chan string)
var clients = make(map[net.Conn]client)
var clientsMutex sync.Mutex

func main() {
	port := "8080"
	listener, err := net.Listen("tcp", ":"+port)
	if err != nil {
		fmt.Printf("Erro ao iniciar o servidor: %s\n", err)
		os.Exit(1)
	}
	defer listener.Close()
	fmt.Printf("Servidor escutando na porta %s\n", port)

	go broadcaster()

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Printf("Erro ao aceitar conexão: %s\n", err)
			continue
		}
		wg.Add(1)
		go handleConnection(conn)
	}
}

func handleConnection(conn net.Conn) {
	defer wg.Done()

	buf := make([]byte, 1024)
	n, err := conn.Read(buf)
	if err != nil {
		fmt.Printf("Erro ao ler nome de usuário: %s\n", err)
		conn.Close()
		return
	}
	username := strings.TrimSpace(string(buf[:n]))

	clientsMutex.Lock()
	clients[conn] = client{conn, username}
	clientsMutex.Unlock()

	fmt.Printf("Cliente '%s' conectado de: %s\n", username, conn.RemoteAddr().String())

	defer func() {
		clientsMutex.Lock()
		delete(clients, conn)
		clientsMutex.Unlock()
		fmt.Printf("Cliente '%s' desconectado: %s\n", username, conn.RemoteAddr().String())
	}()

	for {
		n, err := conn.Read(buf)
		if err != nil {
			if err != io.EOF {
				fmt.Printf("Erro ao ler dados do cliente '%s': %s\n", username, err)
			}
			return
		}
		message := fmt.Sprintf("[%s]: %s\n", username, string(buf[:n]))
		messages <- message
	}
}

func broadcaster() {
	for {
		msg := <-messages
		clientsMutex.Lock()
		for _, c := range clients {
			_, err := c.conn.Write([]byte(msg))
			if err != nil {
				fmt.Printf("Erro ao enviar mensagem para %s: %s\n", c.username, err)
			}
		}
		clientsMutex.Unlock()
	}
}
