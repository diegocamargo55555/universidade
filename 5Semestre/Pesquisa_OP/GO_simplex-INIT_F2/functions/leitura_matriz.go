package matriz

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func Total_de_x() int {
	text, _ := os.Open("texto.txt")
	scanner := bufio.NewScanner(text)
	x_total := 0
	temp := 0

	for scanner.Scan() {
		temp = strings.Count(scanner.Text(), "x")
		if temp > x_total && !strings.Contains(scanner.Text(), "max") {
			x_total = temp
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return x_total
}

func Contar_linhas() int {
	text, _ := os.Open("texto.txt")
	fileScanner := bufio.NewScanner(text)
	lineCount := 0
	for fileScanner.Scan() {
		lineCount++
	}
	return lineCount
}

func Make_matriz() ([][]float64, [][]float64, [][]float64, [][]float64) {
	text, _ := os.Open("texto.txt")
	x_in_FX := Total_de_x()

	linhas := Contar_linhas() - 1
	colunas := linhas + x_in_FX

	var matrix []string
	matrizCT := make([]float64, colunas)

	B_matriz := make([][]float64, linhas)
	for i := 0; i < linhas; i++ {
		B_matriz[i] = make([]float64, 1)
	}

	var numero float64
	var err error
	totalX := x_in_FX + 1
	scanner := bufio.NewScanner(text)
	i := 0

	for scanner.Scan() {
		if !strings.Contains(scanner.Text(), "max") {
			parts := strings.Split(scanner.Text(), "=")
			parts[0] = strings.ReplaceAll(parts[0], " ", "")
			parts[1] = strings.ReplaceAll(parts[1], " ", "")

			//adiciona os x
			if strings.Contains(parts[0], "<") {
				parts[0] = parts[0] + "+x" + strconv.Itoa(totalX)
				parts[0] = strings.Replace(parts[0], "<", "", 1)
			}
			if strings.Contains(parts[0], ">") {
				parts[0] = parts[0] + "-x" + strconv.Itoa(totalX)
				parts[0] = strings.Replace(parts[0], ">", "", 1)
			}

			numero, _ = strconv.ParseFloat(parts[1], 64)
			B_matriz[i][0] = numero
			matrix = append(matrix, string(parts[0]))
			totalX++
			i++
		} else {
			parts := strings.Split(scanner.Text(), "=")
			parts[1] = strings.ReplaceAll(parts[1], " ", "")
			parts[1] = strings.ReplaceAll(parts[1], "-", "+-")
			partes := strings.Split(parts[1], "+")
			for j := 0; j < len(partes); j++ {
				for k := 1; k <= Total_de_x(); k++ {

					if strings.Contains(partes[j], "x"+strconv.Itoa(k)) {
						partes[j] = strings.ReplaceAll(partes[j], "x"+strconv.Itoa(k), "")

						if partes[j] == "" {
							numero = 1
						} else {
							numero, err = strconv.ParseFloat(partes[j], 64)
							if err != nil {
								panic(err)
							}
						}
						matrizCT[k-1] = numero
					}
				}
			}
		}

	}

	CoeNaoBasicos := make([][]float64, 1)
	CoeNaoBasicos[0] = make([]float64, x_in_FX)

	CoeBasicos := make([][]float64, 1)
	CoeBasicos[0] = make([]float64, totalX-x_in_FX-1)

	for i := 0; i < len(matrizCT); i++ {
		if i < len(CoeNaoBasicos[0]) {
			CoeNaoBasicos[0][i] = matrizCT[i]
		} else {
			CoeBasicos[0][i-len(CoeNaoBasicos[0])] = matrizCT[i]
		}
	}
	//fmt.Println("CoeBasicos", CoeBasicos)
	//fmt.Println("CoeNaoBasicos", CoeNaoBasicos)

	matrix_A := make([][]float64, linhas)
	for i := 0; i < linhas; i++ {
		matrix_A[i] = make([]float64, colunas)
	}

	for i := 0; i < len(matrix); i++ {
		matrix[i] = strings.ReplaceAll(matrix[i], "-", "+-")
		partes := strings.Split(matrix[i], "+")

		for j := 0; j < len(partes); j++ {

			for k := 1; k <= colunas; k++ {

				if strings.Contains(partes[j], "x"+strconv.Itoa(k)) {
					partes[j] = strings.ReplaceAll(partes[j], "x"+strconv.Itoa(k), "")

					if partes[j] == "" {
						numero = 1
					} else if partes[j] == "-" {
						numero = -1

					} else {
						numero, err = strconv.ParseFloat(partes[j], 64)
						if err != nil {
							panic(err)
						}
					}

					matrix_A[i][k-1] = numero

				}
			}
		}
	}

	//for i := 0; i < len(matrix); i++ {
	//	fmt.Println("matrix A = B:", matrix_A[i], " = ", B_matriz[i])
	//}

	return matrix_A, B_matriz, CoeBasicos, CoeNaoBasicos
}
