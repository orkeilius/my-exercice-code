/*
 * @lc app=leetcode id=437 lang=typescript
 *
 * [437] Path Sum III
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
function pathSum(root: TreeNode | null, targetSum: number): number {
    if (root == null) return 0

    return (
        pathSum(root.left,targetSum) + 
        pathSum(root.right,targetSum) + 
        dfs(root,targetSum)
    )
};

function dfs(root: TreeNode|null, targetSum: number): number {
    if (root == null) return 0
    targetSum -= root.val

    return (
        (targetSum == 0 ? 1:0 ) + 
        dfs(root.left,targetSum) + 
        dfs(root.right,targetSum) 
    )
}
// @lc code=end

