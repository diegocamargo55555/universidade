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

func Count_x() int {
	text, _ := os.Open("texto.txt")

	scanner := bufio.NewScanner(text)
	x_total := 0
	temp := 0
	// optionally, resize scanner's capacity for lines over 64K, see next example
	for scanner.Scan() {
		temp = strings.Count(scanner.Text(), "x")
		if temp > x_total && !strings.Contains(scanner.Text(), "max") {
			x_total = temp
		}
	}
	//strings.Contains("something", "some")

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

func Make_matriz() [][]string {
	text, _ := os.Open("texto.txt")

	linhas := ""

	var matrix [][]string
	var B_matriz [][]string
	totalX := Count_x() + 1
	scanner := bufio.NewScanner(text)
	i := 0
	for scanner.Scan() {
		if !strings.Contains(scanner.Text(), "max") {
			linhas = strings.Replace(scanner.Text(), "<", "", 1)

			//pega a matrix B
			parts := strings.Split(linhas, "=")
			B_matriz = append(B_matriz, []string{string(parts[1])})

			fmt.Println("tudo: ", linhas)
			println("part1: ", parts[0], "+ x", totalX)

			parteA := ("part1: " + parts[0] + "+ x" + strconv.Itoa(totalX))

			matrix = append(matrix, []string{string(parteA)})
			i++
			totalX++

		}
	}

	fmt.Println("matrizB:", B_matriz)
	fmt.Println("matriX:", matrix)

	return matrix

}
