/*
 * @lc app=leetcode id=104 lang=typescript
 *
 * [104] Maximum Depth of Binary Tree
 */

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

// @lc code=start

function maxDepth(root: TreeNode | null): number {
    if (root == null) { return 0 }
    root.val = 1
    let queue = [root]
    let best = 0

    while (queue.length != 0) {
        let elem = queue.pop() as TreeNode
        best = Math.max(best, elem.val)
        
        if (elem.left !== null) {
            elem.left.val = elem.val + 1
            queue.push(elem.left)
        }
        if (elem.right !== null) {
            elem.right.val = elem.val + 1
            queue.push(elem.right)
        }        
    }
    return best
}

// @lc code=end
