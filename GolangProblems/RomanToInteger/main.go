package main

import (
	"fmt"
	"strings"
)

const (
	DUMMY = "-"
)

var (
	romanMap = map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
)

func romanToInt(s string) int {
	romanStringArray := strings.Split(s, "")

	sum := 0

	for index, romanStr := range romanStringArray {
		if romanStr == DUMMY {
			continue
		}

		if index+1 < len(romanStringArray) {
			currentNumber := convertRomanToInt(romanStr)
			nextNumber := convertRomanToInt(romanStringArray[index+1])

			if currentNumber < nextNumber {
				sum = sum + (nextNumber - currentNumber)
				romanStringArray[index+1] = DUMMY

				continue
			}
		}

		sum += convertRomanToInt(romanStr)
	}

	return sum
}

func convertRomanToInt(s string) int {
	value, ok := romanMap[s]
	if !ok {
		return 0
	}

	return value
}

func main() {
	fmt.Println(romanToInt("V"))
	fmt.Println(romanToInt("IV"))
	fmt.Println(romanToInt("IX"))
	fmt.Println(romanToInt("XV"))
	fmt.Println(romanToInt("XIV"))
	fmt.Println(romanToInt("XX"))
	fmt.Println(romanToInt("MCMXCIV"))
}
