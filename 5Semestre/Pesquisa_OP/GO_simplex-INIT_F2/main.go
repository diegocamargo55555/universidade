package main

import (
	"fmt"
	matriz "main/functions"
)

func main() {

	A_matriz, B_matriz, MZ_matriz := matriz.Make_matriz()

	fmt.Println("a:", A_matriz, "\nb:", B_matriz, "\nmax/min: ", MZ_matriz)

	matriz.Mount_tabela(A_matriz, B_matriz, MZ_matriz)
}
