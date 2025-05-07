package texto

import (
	"bufio"
	"bytes"
	"fmt"
	"log"
	"os"
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
	println("total x: ", x_total)
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

	linhas := "oi"

	var matrix [][]string
	var B_matriz [][]string
	//totalX := Count_x()
	scanner := bufio.NewScanner(text)
	i := 0
	for scanner.Scan() {

		if !strings.Contains(scanner.Text(), "max") {
			linhas = strings.Replace(scanner.Text(), "<", "", 1)

			fmt.Println(string(linhas[1])) // ASCII only

			igual := strings.Index(linhas, "=")

			B_matriz[0][i] = string(linhas[igual])

			//xline := strings.Count(scanner.Text(), "x")

			fmt.Println("teste 1: ", linhas)

			matrix = append(matrix, []string{scanner.Text()})
			i++

		}
	}
	fmt.Println("test_matrix: ")
	fmt.Println(linhas)
	return matrix

}
