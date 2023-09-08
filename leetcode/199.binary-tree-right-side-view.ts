/*
 * @lc app=leetcode id=199 lang=typescript
 *
 * [199] Binary Tree Right Side View
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

function rightSideView(root: TreeNode | null): number[] {
    if (root == null) return []
    let out: number[] = []
    let queue: (TreeNode | null)[] = [root]

    while (queue.length != 0) {
        let outNumber: number | null = null

        let size = queue.length
        for (let i = 0; i < size; i++) {
            let elem = queue.shift()
            if (elem == null) continue

            if (outNumber == null) {
                outNumber = elem.val
            }

            queue.push(elem.right, elem.left)
        }
        if (outNumber != null) {
            out.push(outNumber)
        }
    }

    return out
};
// @lc code=end

