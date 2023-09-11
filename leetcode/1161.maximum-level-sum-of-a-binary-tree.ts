/*
 * @lc app=leetcode id=1161 lang=typescript
 *
 * [1161] Maximum Level Sum of a Binary Tree
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

function maxLevelSum(root: TreeNode | null): number {
    if (root == null) return 0  
    let best = { depth:0,val:Number.NEGATIVE_INFINITY }
    let queue: (TreeNode|null)[] = [root]
    let depth = 1


    while (queue.length != 0) {
        let total: number = 0
        
        let size = queue.length
        for (let i = 0; i < size; i++) {
            let elem = queue.shift()
            if (elem == null) continue

            total += elem.val

            if(elem.right != null) queue.push(elem.right)
            if(elem.left != null) queue.push(elem.left)
        }
        if (total > best.val ){
            best = {depth:depth,val:total}
        }
        depth ++
    }

    return best.depth
};
// @lc code=end

