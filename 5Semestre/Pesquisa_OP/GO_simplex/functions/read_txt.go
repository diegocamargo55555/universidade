package texto

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func Show_txt() {
	fileData, _ := os.ReadFile("texto.txt")

	word := []byte{}
	breakLine := "\n"

	for _, data := range fileData {
		if !bytes.Equal([]byte{data}, []byte(breakLine)) {
			word = append(word, data)
		} else {
			fmt.Printf("ReadLine: %q\n", word)
			word = word[:0]
		}
	}
}

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
	fmt.Println("number of lines:", lineCount)
	return lineCount
}

func Make_matriz() {
	text, _ := os.Open("texto.txt")

	var matrix []string
	var B_matriz []string
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

			B_matriz = append(B_matriz, string(parts[1]))
			matrix = append(matrix, string(parts[0]))

			totalX++
		}
	}

	fmt.Println("matrizB:", B_matriz)
	fmt.Println("matriX:", matrix)

	var matrix_final [3][3]float64

	for i := 0; i < len(matrix); i++ {
		println("\n", i, "----\n")
		fmt.Println("matriX:", matrix)

		matrix[i] = strings.ReplaceAll(matrix[i], "-", "+-")
		partes := strings.Split(matrix[0], "+")
		fmt.Println("partes:", partes)

		for j := 0; j < strings.Count(matrix[i], "+"); j++ {
			println("*", j)

			println("partesJ:", partes[j])
			println("strconv.Itoa(i): x" + strconv.Itoa(i))

			if strings.Contains(partes[j], "x"+strconv.Itoa(i)) {
				println("--match--")

				partes[j] = strings.ReplaceAll(partes[j], "x"+strconv.Itoa(i), "")
				println("parts(valor a ser add):", partes[j])

				numero, err := strconv.ParseFloat(partes[j], 64)
				if err != nil {
					panic(err)
				}

				matrix_final[0][i-1] = numero
			} else {
				println("--not match--")
			}

		}
		fmt.Println("matrix_final:", matrix_final)

	}

	for i := 0; i < len(matrix); i++ {
		fmt.Println("matriX:", matrix[i]+" = "+B_matriz[i])
	}
	fmt.Println("matrix_final:", matrix_final)

}
