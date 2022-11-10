package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}

	if isLeaf(root) {
		return targetSum == root.Val
	}

	newTargetValue := targetSum - root.Val

	return hasPathSum(root.Left, newTargetValue) || hasPathSum(root.Right, newTargetValue)
}

func isLeaf(node *TreeNode) bool {
	return node.Left == nil && node.Right == nil
}

func main() {
	hasPathSum(nil, 3)
}
