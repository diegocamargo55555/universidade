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

func passo1(basica [][]float64, matrizB [][]float64, coeficientesB []float64) [][]float64 {
	basica = matriz.InverterMatriz(basica)
	var fx float64
	//Avaliação da função objetivo:
	for i := 0; i < len(coeficientesB); i++ {
		fx += coeficientesB[i] * matrizB[i][0]
	}
	println(fx)
	return matriz.Multiplicacao(basica, matrizB) // Resolva o sistema BxB = b ou xB = B −1 b e obtenha x̂B
}

func passo2(basica [][]float64, coeficientesN []float64, coeficientesB []float64, Nbasica [][]float64)  {
	basica = matriz.InverterMatriz(basica)
	cb := matriz.Multiplicacao(basica, coeficientesB)
	//basica * coeficientes

	//custos relativos 2.2
	//ĉ1 = c1 − λT * a1             = coe - matriz.Multiplicacao(CB, basica) * Nbasica
	var cresult []float64
	for _, coe := range coeficientesN {
		cresult = append(cresult, (coe - matriz.Multiplicacao()[][]))
	}
}

func passo4(basica [][]float64, Nbasica [][]float64)  {
	//   y = B a2   ===       

	y := matriz.InverterMatriz(basica) * Nbasica
}

func passo5()  {
	
}