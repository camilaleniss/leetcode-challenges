package main

import "fmt"

func numTrees(n int) int {
	if n < 2 {
		return 1
	}

	dp := make([]int, n+1)
	dp[0] = 1
	dp[1] = 1

	for k := 2; k <= n; k++ {
		for i := 0; i < k; i++ {
			dp[k] += dp[i] * dp[k-i-1]
		}
	}

	return dp[n]
}

func main() {
	fmt.Println(numTrees(1))
	fmt.Println(numTrees(2))
	fmt.Println(numTrees(3))
	fmt.Println(numTrees(4))
	fmt.Println(numTrees(5))
	fmt.Println(numTrees(6))
}
