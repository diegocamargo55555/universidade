package main

import (
	"fmt"
	matriz "main/functions"
)

func main() {

	var B_matriz []float64
	var A_matriz [][]float64

	A_matriz, B_matriz = matriz.Make_matriz()

	fmt.Println("a:", A_matriz, "\nb:", B_matriz)

}
