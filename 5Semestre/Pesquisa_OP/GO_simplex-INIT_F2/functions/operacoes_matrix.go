package matriz

import (
	"math"
)

func InverterMatriz(matriz [][]float64) [][]float64 {
	linhas := len(matriz)
	if linhas == 0 {
		return [][]float64{}
	}
	colunas := len(matriz[0])
	if colunas == 0 {
		return [][]float64{}
	}

	matrizInvertida := make([][]float64, colunas)
	for i := range matrizInvertida {
		matrizInvertida[i] = make([]float64, linhas)
	}

	for i := 0; i < linhas; i++ {
		for j := 0; j < colunas; j++ {
			matrizInvertida[j][i] = matriz[i][j]
		}
	}

	return matrizInvertida
}

func Determinante(matriz [][]float64) float64 {
	n := len(matriz)
	if n != len(matriz[0]) {
		panic("A matriz não é quadrada")
	}

	if n == 1 {
		return matriz[0][0]
	}

	if n == 2 {
		return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
	}

	det := 0.0
	for k := 0; k < n; k++ {
		submatriz := make([][]float64, n-1)
		for i := range submatriz {
			submatriz[i] = make([]float64, n-1)
		}

		valorI := 0
		for i := 1; i < n; i++ {
			valorJ := 0
			for j := 0; j < n; j++ {
				if j != k {
					submatriz[valorI][valorJ] = matriz[i][j]
					valorJ++
				}
			}
			valorI++
		}
		det += matriz[0][k] * math.Pow(-1, float64(k)) * Determinante(submatriz)
	}

	return det
}

func Multiplicacao(a [][]float64, b [][]float64) [][]float64 {
	linhaA := len(a)
	colunaA := len(a[0])
	colunaB := len(b[0])

	if colunaA != len(b) {
		panic("número de colunas da primeira matriz deve ser igual ao número de linhas da segunda")
	}

	result := make([][]float64, linhaA)
	for i := range result {
		result[i] = make([]float64, colunaB)
	}

	for i := 0; i < linhaA; i++ {
		for j := 0; j < colunaB; j++ {
			for k := 0; k < colunaA; k++ {
				result[i][j] += a[i][k] * b[k][j]
			}
		}
	}

	return result
}
