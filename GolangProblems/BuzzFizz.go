package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	SuccessTemplate    = "SUCCESS => RECEIVED: %d"
	FailureTemplate    = "FAILURE => RECEIVED: %d, EXPECTED: %d"
	WrongInputTemplate = "FAILURE => WRONG INPUT (LINE %d)"

	ErrWrongInput = errors.New("wrong input found in line")

	reader = bufio.NewReader(os.Stdin)
)

func readInputs(numberOfLines int) []string {
	lines := []string{}

	for i := 0; i < numberOfLines; i++ {
		line, _ := reader.ReadString('\n')
		line = strings.ReplaceAll(line, "\n", "")

		lines = append(lines, line)
	}

	return lines
}

func convertLine(line string) []int {
	items := strings.Split(line, " ")

	convertedList := []int{}

	for _, item := range items {
		if item == "" {
			continue
		}

		convertedItem, err := strconv.Atoi(item)
		if err != nil {
			return []int{}
		}

		if convertedItem < 0 {
			return []int{}
		}

		convertedList = append(convertedList, convertedItem)
	}

	return convertedList
}

func reviewBatches(lines []string) []string {
	responses := []string{}

	for i, line := range lines {
		response := reviewLine(line, i)

		responses = append(responses, response)
	}

	return responses
}

func reviewLine(line string, lineNumber int) string {
	itemsList := convertLine(line)

	if len(itemsList) < 1 {
		return fmt.Sprintf(WrongInputTemplate, lineNumber+2)
	}

	maximum := getMaximum(itemsList)

	if maximum != len(itemsList) {
		return fmt.Sprintf(FailureTemplate, len(itemsList), maximum)
	}

	return fmt.Sprintf(SuccessTemplate, maximum)
}

func getMaximum(items []int) int {
	maximum := 0

	for _, item := range items {
		if item > maximum {
			maximum = item
		}
	}

	return maximum
}

func logResponses(responses []string) {
	for _, response := range responses {
		fmt.Println(response)
	}
}

func main() {
	text, _ := reader.ReadString('\n')
	text = strings.ReplaceAll(text, "\n", "")

	numberOfLines, err := strconv.Atoi(text)
	if err != nil {
		fmt.Printf(WrongInputTemplate, 1)

		return
	}

	if numberOfLines < 1 {
		return
	}

	lines := readInputs(numberOfLines)

	responses := reviewBatches(lines)

	logResponses(responses)
}
