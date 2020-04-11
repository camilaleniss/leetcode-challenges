package JavaProblems;

public class DiameterBinaryTree {

    public static int diameterOfBinaryTree(TreeNode root) {
        if (root == null)
            return 0;

        Diameter diameter = new Diameter();
        int height_tree = getHeight(root, diameter);
        return diameter.diameter - 1;
    }

    public static int getHeight(TreeNode node, Diameter diameter){
        if (node == null)
            return 0;

        int left_subtree_height = getHeight(node.left, diameter);
        int right_subtree_height = getHeight(node.right, diameter);

        diameter.diameter = Math.max(diameter.diameter, 1 + left_subtree_height + right_subtree_height);

        return 1 + Math.max(left_subtree_height, right_subtree_height );
    }

    static class Diameter{
        int diameter = 0;
    }

    public static void main (String [] args){
        
        TreeNode root = new TreeNode(1);
        TreeNode node1 = new TreeNode(2);
        TreeNode node2 = new TreeNode(3);
        TreeNode node3 = new TreeNode(4);
        TreeNode node4 = new TreeNode(5);
        node1.left = node3;
        node1.right = node4;
        root.left = node1;
        root.right = node2;
        
        /*
        TreeNode root = new TreeNode(1);
        TreeNode node1 = new TreeNode(2);
        TreeNode node2 = new TreeNode(3);
        TreeNode node3 = new TreeNode(4);
        TreeNode node4 = new TreeNode(5);
        TreeNode node5 = new TreeNode(6);
        TreeNode node6 = new TreeNode(7);

        node5.right = node6;
        node4.right = node5;
        node1.right = node4;
        node1.left = node3;
        root.left = node1;
        root.right = node2;
        */
        System.out.println(diameterOfBinaryTree(root));
    } 
    

}