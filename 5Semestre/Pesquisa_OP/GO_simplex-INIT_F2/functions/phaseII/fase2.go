package phaseII

import (
	"fmt"
	matriz "main/functions"
)

func Mount_tabela(matrizA [][]float64, matrizB [][]float64, matrixCoeB [][]float64, matrixCoeN [][]float64) {
	println("fase 2")
	//fmt.Println("matrizA", matrizA)
	//fmt.Println("matrizB", matrizB)
	//fmt.Println("matrixCoeB", matrixCoeB)
	//fmt.Println("matrixCoeN", matrixCoeN)
	linhas := len(matrizB)
	//pega a matrix nao basica BN
	nao_basicasBN := make([][]float64, linhas)
	for i := 0; i < linhas; i++ {
		nao_basicasBN[i] = make([]float64, len(matrixCoeN[0]))
	}
	for i := 0; i < linhas; i++ {
		for j := 0; j < len(matrixCoeN[0]); j++ {
			nao_basicasBN[i][j] = matrizA[i][j]
		}
	}

	//pega a matrix basica BN
	basicasBN := make([][]float64, linhas)
	for i := 0; i < linhas; i++ {
		basicasBN[i] = make([]float64, len(matrixCoeB[0]))
	}

	for i := 0; i < linhas; i++ {
		for j := 1; j <= len(matrixCoeB[0]); j++ {
			basicasBN[i][linhas-j] = matrizA[i][len(matrizA[0])-j]
		}
	}
	//fmt.Println("nao_basicasBN", nao_basicasBN)
	//fmt.Println("basicasBN", basicasBN)

	println("-------")
	XB := passo1(basicasBN, matrizB, matrixCoeB[0])
	fmt.Println("XB: ", XB)

	passo2(basicasBN, matrixCoeB, matrixCoeN, nao_basicasBN)
	//println("p1: ", p1)

	fmt.Println("solucao otima:", passo3(matrixCoeN))

	y := passo4(basicasBN, nao_basicasBN)
	fmt.Println("Y:", y)

	passo5()

}

func passo1(basica [][]float64, matrizB [][]float64, coeficientesBasicos []float64) [][]float64 {
	basica = matriz.InverterMatriz(basica)
	//fmt.Println("coeficientesBasicos", coeficientesBasicos)
	//fmt.Println("matrizB", matrizB)
	var fx float64
	//Avaliação da função objetivo:
	for i := 0; i < len(matrizB); i++ {
		fmt.Println("CBi * XBi =", coeficientesBasicos[i], "*", matrizB[i][0])
		fx += coeficientesBasicos[i] * matrizB[i][0]
	}
	fmt.Println("fx:", fx)
	return matriz.Multiplicacao(basica, matrizB) // Resolva o sistema BxB = b ou xB = B −1 b e obtenha x̂B
}

func passo2(basica [][]float64, basicasBN [][]float64, matrixCoeB [][]float64, nao_basicasBN [][]float64) {
	basica = matriz.InverterMatriz(basica)
	lambda := matriz.Multiplicacao(basicasBN, basica)

	//custos relativos 2.2
	//ĉ1 = c1 − λT * a1             = coe - matriz.Multiplicacao(basica, CB) * Nbasica
	//var cresult []float64

	nao_basicas_N1 := make([][]float64, len(nao_basicasBN))
	for i := 0; i < len(nao_basicasBN); i++ {
		nao_basicas_N1[i] = make([]float64, 1)
	}
	i := 0
	a := matriz.Multiplicacao(lambda, nao_basicas_N1)

	fmt.Println("lambda *  nao_basicas_N1", a)
	custo1 := matrixCoeB[0][i] - a[0][0]
	custo2 := matrixCoeB[0][i+1] - a[0][0]

	fmt.Println("a ", custo1)
	fmt.Println("a2 ", custo2)

	//2.3) {determinação da variável a entrar na base}:

}

func passo3(matrixCoeN [][]float64) bool {
	for i := 0; i < len(matrixCoeN[0]); i++ {
		if matrixCoeN[0][i] < 0 {
			return false
		}
	}
	panic("A solução ótima")
}

func passo4(basica [][]float64, Nbasica [][]float64) [][]float64 {
	//   y = B a2
	basica = matriz.InverterMatriz(basica)
	//y := basica * Nbasica
	nao_basicas_N2 := make([][]float64, len(Nbasica))
	for i := 0; i < len(Nbasica); i++ {
		nao_basicas_N2[i] = make([]float64, 1)
	}
	for i := 0; i < len(Nbasica); i++ {
		nao_basicas_N2[i][0] = Nbasica[i][1]
	}

	y := matriz.Multiplicacao(basica, nao_basicas_N2)
	return y

}

func passo5() {

}
