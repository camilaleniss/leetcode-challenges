package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// A complete binary tree can have at most (2^h – 1) nodes in total where h is the height of the tree
// (This happens when all the levels are completely filled).
func countNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}

	leftHeight := countLeftHeight(root)
	rightHeight := countRightHeight(root)

	if leftHeight == rightHeight {
		return int(math.Pow(2, float64(leftHeight))) - 1
	}

	return 1 + countNodes(root.Left) + countNodes(root.Right)
}

func countLeftHeight(node *TreeNode) int {
	height := 0

	for {
		if node == nil {
			break
		}

		height++

		node = node.Left
	}

	return height
}

func countRightHeight(node *TreeNode) int {
	height := 0

	for {
		height++
		node = node.Right

		if node == nil {
			break
		}
	}

	return height
}

func main() {
	root := TreeNode{}
	root.Left = &TreeNode{}
	root.Right = &TreeNode{}

	fmt.Println(countNodes(&root))

	root.Left.Left = &TreeNode{}
	root.Left.Right = &TreeNode{}

	fmt.Println(countNodes(&root))

	root.Left.Left.Left = &TreeNode{}

	fmt.Println(countNodes(&root))

}
