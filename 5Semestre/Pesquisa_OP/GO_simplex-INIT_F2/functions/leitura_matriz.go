package matriz

import (
	"bufio"
	"fmt"
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

func Make_matriz() ([][]float64, []float64, []float64) {
	text, _ := os.Open("texto.txt")
	linhas := Contar_linhas() - 1
	colunas := linhas + Total_de_x()

	var matrix []string
	var B_matriz []float64
	matrizCT := make([]float64, colunas)

	var numero float64
	var err error

	totalX := Total_de_x() + 1
	scanner := bufio.NewScanner(text)

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
			B_matriz = append(B_matriz, numero)
			matrix = append(matrix, string(parts[0]))
			totalX++
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
	fmt.Println("\nBasica: ", matrizCT)
	// get_number_linha

	matrix_final := make([][]float64, linhas)
	for i := 0; i < linhas; i++ {
		matrix_final[i] = make([]float64, colunas)
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
					} else {
						numero, err = strconv.ParseFloat(partes[j], 64)
						if err != nil {
							panic(err)
						}
					}
					matrix_final[i][k-1] = numero
				}
			}
		}
	}
	for i := 0; i < len(matrix); i++ {
		fmt.Println("matrix A = B:", matrix_final[i], " = ", B_matriz[i])
	}

	return matrix_final, B_matriz, matrizCT
}

func Mount_tabela(matrizA [][]float64, matrizB []float64, matrizM []float64) {

}
