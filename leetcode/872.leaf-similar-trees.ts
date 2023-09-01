/*
 * @lc app=leetcode id=872 lang=typescript
 *
 * [872] Leaf-Similar Trees
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

function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {

    let leafs: number[] = [], queue = [root1]
    
    while (queue.length != 0) {
        let elem = queue.pop() as TreeNode
        
        if (elem.left == null && elem.right == null) {
            leafs.push(elem.val)
            continue
        }

        if (elem.right !== null) {
            queue.push(elem.right)
        }        
        if (elem.left !== null) {
            queue.push(elem.left)
        }
    }

    queue = [root2]
    while (queue.length != 0) {
        let elem = queue.pop() as TreeNode
        
        if (elem.left == null && elem.right == null) {
            if (leafs.shift() != elem.val) {
                return false
            }
            continue
        }

        if (elem.right !== null) {
            queue.push(elem.right)
        }        
        if (elem.left !== null) {
            queue.push(elem.left)
        }
    }

    return leafs.length == 0
};
// @lc code=end

