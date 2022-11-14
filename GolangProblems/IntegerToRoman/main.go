package main

import (
	"fmt"
	"strconv"
	"strings"
)

var (
	position = map[int]int{
		1: 1,
		2: 10,
		3: 100,
		4: 1000,
	}

	romanLowerMap = map[int]string{
		1:    "I",
		10:   "X",
		100:  "C",
		1000: "M",
	}

	romanUpperMap = map[int]string{
		1:   "V",
		10:  "L",
		100: "D",
	}

	fourMap = map[int]string{
		1:   "IV",
		10:  "XL",
		100: "CD",
	}

	nineMap = map[int]string{
		1:   "IX",
		10:  "XC",
		100: "CM",
	}
)

func intToRoman(num int) string {
	integerArray := strings.Split(fmt.Sprintf("%d", num), "")

	romanString := ""
	positionCounter := 1

	for i := len(integerArray) - 1; i > -1; i-- {
		value := integerArray[i]

		valuePos, ok := position[positionCounter]
		if !ok {
			continue
		}

		convertedValue, _ := strconv.Atoi(value)

		part := converIntToRoman(convertedValue, valuePos)

		romanString = part + romanString

		positionCounter++
	}

	return romanString
}

func converIntToRoman(num int, pos int) string {
	if num == 0 {
		return ""
	}

	if num == 4 {
		return fourMap[pos]
	}

	if num == 9 {
		return nineMap[pos]
	}

	if num > 4 {
		return fmt.Sprintf("%s%s", romanUpperMap[pos], converIntToRoman(num-5, pos))
	}

	return strings.Repeat(romanLowerMap[pos], num)
}

func main() {
	fmt.Println(intToRoman(1))
	fmt.Println(intToRoman(4))
	fmt.Println(intToRoman(5))
	fmt.Println(intToRoman(7))
	fmt.Println(intToRoman(9))
	fmt.Println(intToRoman(10))
	fmt.Println(intToRoman(14))
	fmt.Println(intToRoman(20))
	fmt.Println(intToRoman(58))
	fmt.Println(intToRoman(1994))
}
