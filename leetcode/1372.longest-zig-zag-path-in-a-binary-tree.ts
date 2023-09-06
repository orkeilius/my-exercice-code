/*
 * @lc app=leetcode id=1372 lang=typescript
 *
 * [1372] Longest ZigZag Path in a Binary Tree
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

interface queueItem{
    node: TreeNode
    IsLeft: boolean
    length : number
}

function longestZigZag(root: TreeNode | null): number {

    if(root == null) return 0
    
    let best = 0
    let queue: queueItem[] = [{ node: root, IsLeft: true, length: -1 }];
    
    while (queue.length != 0) {
        let elem = queue.pop() as queueItem

        best = Math.max(best, elem.length)

        if (elem.node.left != null) {
            queue.push({node: elem.node.left, IsLeft : true, length : !elem.IsLeft? elem.length+1 : 0})
        }
        if (elem.node.right != null) {
            queue.push({node: elem.node.right, IsLeft : false, length : elem.IsLeft? elem.length+1 : 0})

        } 
    }

    return best
};
// @lc code=end

