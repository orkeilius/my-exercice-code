/*
 * @lc app=leetcode id=450 lang=typescript
 *
 * [450] Delete Node in a BST
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

function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
    
    if (root == null ) return null
    let out = new TreeNode(-1,null,root)
    let previous = out
    let pointer :TreeNode|null = root
    
    while (pointer != null && pointer?.val != key) {
        previous = pointer
        if (pointer.val < key) pointer = pointer.right
        else pointer = pointer.left 
    }

    let node2Add: TreeNode[] = []
    if (pointer?.left != null) node2Add.push(pointer?.left )
    if (pointer?.right != null) node2Add.push(pointer?.right)
    
    if (previous.val <  key) {
        previous.right = node2Add.length != 0 ? node2Add.pop() as TreeNode : null
    }
    else {
        previous.left = node2Add.length != 0 ? node2Add.pop() as TreeNode : null
    } 

    if (node2Add.length != 0) {
        let node = node2Add.pop() as TreeNode
        pointer = previous
        
        while (pointer != null) {
            if (pointer.val < node.val) {
                if (pointer.right == null) {
                    pointer.right = node
                    break
                }
                pointer = pointer.right
            }
            else {
                if (pointer.left == null) {
                    pointer.left = node
                    break
                }
                pointer = pointer.left
            }
        }
    }

        return out.right
};
// @lc code=end

