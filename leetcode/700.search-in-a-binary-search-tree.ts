/*
 * @lc app=leetcode id=700 lang=typescript
 *
 * [700] Search in a Binary Search Tree
 */

class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

// @lc code=start

function searchBST(root: TreeNode | null, val: number): TreeNode | null {
    
    if (root == null) return null
    
    let queue: TreeNode[] = [root]

    while (queue.length != 0) {        
        let elem = queue.pop()

        if (elem == null) continue

        if (elem.val == val) {
            return elem
        }
        
        if(elem.right != null) queue.push(elem.right)
        if(elem.left != null) queue.push(elem.left)
    }
    return null


};
// @lc code=end

