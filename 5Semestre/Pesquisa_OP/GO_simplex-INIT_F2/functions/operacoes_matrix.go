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
	for j := 0; j < n; j++ {
		submatriz := make([][]float64, n-1)
		for i := range submatriz {
			submatriz[i] = make([]float64, n-1)
		}

		for i := 1; i < n; i++ {
			col := 0
			for k := 0; k < n; k++ {
				if k != j {
					submatriz[i-1][col] = matriz[i][k]
					col++
				}
			}
		}
		termo := matriz[0][j] * Determinante(submatriz)
		det += math.Pow(-1, float64(j)) * termo
	}
	return det
}

func Multiplicacao(a [][]float64, b [][]float64) [][]float64 {
	if len(a[0]) != len(b) {
		panic("número de colunas da primeira matriz deve ser igual ao número de linhas da segunda")
	}

	linhaA := len(a)
	colunaA := len(a[0])
	colunaB := len(b[0])

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
