package main

import (
	matriz "main/functions"
	"main/functions/phaseII"
)

func main() {

	A_matriz, B_matriz, CoeBasicos, CoeNaoBasicos := matriz.Make_matriz()
	//fmt.Println("CoeBasicos/CoeNaoBasicos: ", CoeBasicos, CoeNaoBasicos)

	phaseII.Mount_tabela(A_matriz, B_matriz, CoeBasicos, CoeNaoBasicos)
}
