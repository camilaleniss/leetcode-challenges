package main

import "fmt"

var (
	pick = 1994
)

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */
func guess(num int) int {
	if num > pick {
		return -1
	}

	if num < pick {
		return 1
	}

	return 0
}

func guessNumber(n int) int {
	guessResponse := guess(n)
	if guessResponse == 0 {
		return n
	}

	start := 1
	end := n

	for {
		picked := start + (end-start)/2

		guessResponse := guess(picked)

		if guessResponse == -1 {
			end = picked - 1
		}

		if guessResponse == 1 {
			start = picked + 1
		}

		if guessResponse == 0 {
			return picked
		}
	}
}

func main() {
	response := guessNumber(10000)
	fmt.Printf("Response: %d\n", response)
}
