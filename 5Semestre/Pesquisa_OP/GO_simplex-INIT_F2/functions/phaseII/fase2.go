package phaseII

import (
	"fmt"
	matriz "main/functions"
)

func Mount_tabela(matrizA [][]float64, matrizB []float64, matrizM []float64) {

	var nao_basicas []float64
	nx := 0
	for _, i := range matrizM {
		if i != 0 {
			nao_basicas = append(nao_basicas, i)
			nx++
		}
	}

	nx = len(matrizA[0]) - nx
	println(nx)
	linhas := len(matrizB)

	//pega a matrix nao basica BN
	nao_basicasBN := make([][]float64, linhas)
	for i := 0; i < linhas; i++ {
		nao_basicasBN[i] = make([]float64, nx)
	}
	for i := 0; i < nx; i++ {
		for j := 0; j < nx; j++ {
			nao_basicasBN[i][j] = matrizA[i][j]
		}
	}

	//pega a matrix basica BN
	basicasBN := make([][]float64, linhas)
	for i := 0; i < linhas; i++ {
		basicasBN[i] = make([]float64, nx)
	}
	for i := 0; i < nx; i++ {
		for j := 1; j < nx+1; j++ {
			basicasBN[i][linhas-j] = matrizA[i][len(matrizA[0])-j]
		}
	}

	coeficientes := make([]float64, len(matrizM))
	for i := 1; i <= len(matrizM); i++ {
		coeficientes[i-1] = matrizM[len(matrizM)-i]
	}

	for i := 0; i < len(nao_basicasBN); i++ {
		fmt.Println("nao_basicasBN:", nao_basicasBN[i])
	}
	for i := 0; i < len(basicasBN); i++ {
		fmt.Println("basicasBN:", basicasBN[i])
	}
	fmt.Println("coeficientes:", coeficientes)

}

func passo1(basica [][]float64, matrizB []float64) {
	basica = matriz.InverterMatriz(basica)
	//basica * matriz
}

func passo2(basica [][]float64, coeficientes []float64) {
	basica = matriz.InverterMatriz(basica)
	//basica * coeficientes

	//custos relativos 2.2

}
