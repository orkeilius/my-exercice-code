/*
 * @lc app=leetcode id=1448 lang=typescript
 *
 * [1448] Count Good Nodes in Binary Tree
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
    max : number
}

function goodNodes(root: TreeNode | null): number {
    if (root == null) { return 0 }
    let queue: queueItem[] = [{ node: root,max: Number.NEGATIVE_INFINITY }]
    let total = 0

    while (queue.length != 0) {
        let elem = queue.pop() as queueItem
        if(elem.node.val >= elem.max){total++}

        elem.max = Math.max(elem.max, elem.node.val)
        
        if (elem.node.left !== null) {
            queue.push({node: elem.node.left ,max: elem.max})
        }
        if (elem.node.right !== null) {
            queue.push({node: elem.node.right ,max: elem.max})
        }        
    }
    return total
};
// @lc code=end

