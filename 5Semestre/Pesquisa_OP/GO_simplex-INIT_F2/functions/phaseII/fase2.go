package phaseII

import (
	"fmt"
	matriz "main/functions"
)

func Mount_tabela(matrizA [][]float64, matrizB [][]float64, CoeB [][]float64, CoeN [][]float64) {
	menorZero := true
	//for menorZero {
	for i := 0; i < 3; i++ {

		println("fase 2 iteracao:")
		//fmt.Println("matrizA", matrizA)
		//fmt.Println("matrizB", matrizB)
		//fmt.Println("CoeB", CoeB)
		//fmt.Println("CoeN", CoeN)
		linhas := len(matrizB)
		//pega a matrix nao basica BN
		nao_basicasN := make([][]float64, linhas)
		for i := 0; i < linhas; i++ {
			nao_basicasN[i] = make([]float64, len(CoeN[0]))
		}
		for i := 0; i < linhas; i++ {
			for j := 0; j < len(CoeN[0]); j++ {
				nao_basicasN[i][j] = matrizA[i][j]
			}
		}

		//pega a matrix basica BN
		basicasBN := make([][]float64, linhas)
		for i := 0; i < linhas; i++ {
			basicasBN[i] = make([]float64, len(CoeB[0]))
		}
		for i := 0; i < linhas; i++ {
			for j := 1; j <= len(CoeB[0]); j++ {
				basicasBN[i][linhas-j] = matrizA[i][len(matrizA[0])-j]
			}
		}
		//fmt.Println("nao_basicasN", nao_basicasN)
		//fmt.Println("basicasBN", basicasBN)

		println("-------")
		XB := passo1(basicasBN, matrizB, CoeB[0])
		fmt.Println("XB: ", XB)

		custo, posi := passo2(basicasBN, CoeB, CoeN, nao_basicasN)
		//println("p1: ", p1)
		menorZero = passo3(custo[0][posi])
		fmt.Println("solucao otima:", menorZero)

		y := passo4(basicasBN, nao_basicasN) // Cálculo da direção simplex
		fmt.Println("Y:", y)

		posicaoSBasica := passo5(y, XB)
		println("posicaoSBasica:", posicaoSBasica)
		if menorZero {
			//trocaPosicoes(matrizB, CoeB, nao_basicasN, CoeN, posicaoSBasica, posi)
			//                trocarPosicoesBeN(&matrizB, &coeficientesB, &nao_basicasN, &coeficientesN, posicaoSBasica, posSairN, &posicoes, &posicoesN);
			trocaPosicoes(matrizB [][]float64, coeficientesB [][]float64, nao_basicasN [][]float64, coeficientesN [][]float64, posicaoSBasica int, posicaoSairN int, posicoes []int, posicoesN []int) {

		}

	}
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

func passo2(basicasBN [][]float64, CoeB [][]float64, CoeN [][]float64, nao_basicasN [][]float64) ([][]float64, int) {
	basicasBN = matriz.InverterMatriz(basicasBN)
	lambda := matriz.Multiplicacao(CoeB, basicasBN)

	//custos relativos 2.2
	//ĉ1 = c1 − λT * a1             = coe - matriz.Multiplicacao(basica, CB) * Nbasica
	//var cresult []float64

	nao_basicas_N1 := make([][]float64, len(nao_basicasN))
	for i := 0; i < len(nao_basicasN); i++ {
		nao_basicas_N1[i] = make([]float64, 1)
	}
	a := matriz.Multiplicacao(lambda, nao_basicas_N1)
	var posi int
	// cn -0 a

	fmt.Println("lambda *  nao_basicas_N1", a)

	custo := make([][]float64, 1)
	custo[0] = make([]float64, len(CoeN))

	for i := 0; i < len(custo[0]); i++ {
		custo[0][i] = CoeN[0][i] - a[0][0]
		posi = i
		fmt.Println("custo ", custo[0][i])

	}
	return custo, posi
	//2.3) {determinação da variável a entrar na base}:

}

func passo3(CoeN float64) bool {
	if CoeN < 0 {
		return true
	}
	return false

	//panic("P3: A solução ótima")
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

func passo6(y1 float64, xB1 float64, y2 float64, xB2 float64) {
	div1 := xB1 / y1
	div2 := xB2 / y2

	fmt.Println("xB1 / y1:", xB1, "/", y1)
	fmt.Println("xB2 / y2:", xB2, "/", y2)

	var Emin float64
	if div1 < div2 {
		Emin = div1
	} else {
		Emin = div2
	}
	println("Emin", Emin)
}

func passo5(y [][]float64, xB [][]float64) int {
	Emin := xB[0][0] / y[0][0]
	posi := 0
	var temp float64

	for i := 0; i < len(xB); i++ {
		if y[i][0] > 0 {
			temp = xB[i][0] / y[i][0]
			if temp < Emin {
				Emin = temp
				posi = i
			}
		}
	}
	fmt.Println("Emin:", Emin)
	return posi
}

func trocaColuna(matrizB [][]float64, nao_basicasN [][]float64, posiB int, posiN int) ([][]float64, [][]float64) {
	tamB := len(matrizB)
	temp := make([]float64, tamB)

	for i := 0; i < tamB; i++ {
		temp[i] = matrizB[i][posiN]
	}
	for i := 0; i < tamB; i++ {
		matrizB[i][posiB] = matrizB[i][posiN]
	}
	for i := 0; i < tamB; i++ {
		nao_basicasN[i][posiN] = temp[i]
	}
	return matrizB, nao_basicasN

}

func trocaPosicoes(matrizB [][]float64, coeficientesB [][]float64, nao_basicasN [][]float64, coeficientesN [][]float64, posicaoSBasica int, posicaoSairN int, posicoes []int, posicoesN []int) {
	trocaColuna(matrizB, nao_basicasN, posicaoSBasica, posicaoSairN)
	trocaColuna(coeficientesB, coeficientesN, posicaoSBasica, posicaoSairN)
	temp := posicoesN[posicaoSairN]
	posicoesN[posicaoSairN] = posicoes[posicaoSBasica]
	posicoes[posicaoSBasica] = temp
}
