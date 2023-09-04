/*
 * @lc app=leetcode id=141 lang=typescript
 *
 * [141] Linked List Cycle
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

function hasCycle(head: ListNode | null): boolean {
    let slow: ListNode | null | undefined = head
    let fast: ListNode | null | undefined = head?.next
    
    while (fast != null && fast != undefined && slow != fast) {
        slow = slow?.next 
        fast = fast?.next?.next 
    }
    return fast != null 
};
// @lc code=end

