/*
 * @lc app=leetcode id=236 lang=typescript
 *
 * [236] Lowest Common Ancestor of a Binary Tree
 */

class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

// @lc code=start

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    if (root == null || p == null || q ==null) return null

    function dfs(node): number | TreeNode {
        let total = 0
        if (node.left != null) {
            let result = dfs(node.left)
            if (typeof result != "number") return result
            total += result
        }
        if (node.right != null) {
            let result = dfs(node.right)
            if (typeof result != "number") return result
            total += result
        }
        if (node == q || node == p) total++

        if (total == 2) {
            return node
        }
        else {
            return total
        }
    }
    return dfs(root) as TreeNode
};

// @lc code=end

