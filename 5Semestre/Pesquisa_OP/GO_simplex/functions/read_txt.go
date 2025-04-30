package texto

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
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

func Count_x(text io.Reader) int {
	msg := "Lorem ipsum example of lorem ipsum."
	fmt.Printf("contains %d occurences of ipsum \n", strings.Count(msg, "ipsum"))

	scanner := bufio.NewScanner(text)
	i := 0
	// optionally, resize scanner's capacity for lines over 64K, see next example
	for scanner.Scan() {
		println("i:", i)
		i++
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	x_total := strings.Count(msg, "x")
	return x_total

}

func Contar_linhas(text io.Reader) int {
	fileScanner := bufio.NewScanner(text)
	lineCount := 0
	for fileScanner.Scan() {
		lineCount++
	}
	fmt.Println("number of lines:", lineCount)
	return lineCount
}
