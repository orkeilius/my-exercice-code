/*
 * @lc app=leetcode id=206 lang=typescript
 *
 * [206] Reverse Linked List
 */

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

// @lc code=start
function reverseList(head: ListNode | null): ListNode | null {
    if(head == null){return null}
    let reverse = new ListNode(head.val)
    while (head.next != null) {
        head = head.next
        reverse = new ListNode(head.val,reverse)
    }
    return reverse
};
// @lc code=end

