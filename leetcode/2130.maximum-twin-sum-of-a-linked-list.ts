/*
 * @lc app=leetcode id=2130 lang=typescript
 *
 * [2130] Maximum Twin Sum of a Linked List
 */

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

// @lc code=start

function pairSum(head: ListNode | null): number {
    let pointerLength = head, pointer = head
    let stack :number[]= []
    while (pointerLength?.next != null) {
        stack.push(pointer?.val)

        pointerLength = pointerLength.next.next
        pointer = pointer?.next
    }

    let best = 0
    while (stack.length > 0) {
        best = Math.max(best, stack.pop() + pointer?.val)
        pointer = pointer?.next    
    }
    return best
};
// @lc code=end

