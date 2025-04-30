package main

import (
	texto "main/functions"
	"os"
)

func main() {
	text, _ := os.Open("texto.txt")

	// texto.Show_txt()
	//	texto.Contar_linhas(text)

	texto.Count_x(text)
}
