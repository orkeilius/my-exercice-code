
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


class Solution {
    public int averageOfSubtree(TreeNode root) {
        
        int[] values = subtree(root);
        return values[2]; // nbGood
    }

    public int[] subtree(TreeNode root){

        int[] valuesLeft = new int[] { 0, 0, 0 };
        if (root.left != null) {
            valuesLeft = subtree(root.left);
        }

        int[] valuesRight = new int[] { 0, 0, 0 };
        if (root.right != null) {
            valuesRight = subtree(root.right);
        }

        int total = valuesLeft[0] + valuesRight[0] + root.val;
        int nbNode = valuesLeft[1] + valuesRight[1] + 1;
        int nbGood = valuesLeft[2] + valuesRight[2];

        if (total / nbNode == root.val) {
            nbGood++;
        }

        return new int[] { total, nbNode, nbGood };
    }
}