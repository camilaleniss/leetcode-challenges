package main

import "fmt"

func containsDuplicate(nums []int) bool {
	numbersMap := map[int]bool{}

	for _, number := range nums {
		_, ok := numbersMap[number]

		if ok {
			return true
		}

		numbersMap[number] = true
	}

	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3}))
	fmt.Println(containsDuplicate([]int{3, 2, 3}))
	fmt.Println(containsDuplicate([]int{-1, 1, 3}))
}
