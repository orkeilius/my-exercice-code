/*
 * @lc app=leetcode id=2095 lang=typescript
 *
 * [2095] Delete the Middle Node of a Linked List
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
function deleteMiddle(head: ListNode | null): ListNode | null {
    if(head?.next == null){
        return null
    }
    let pointer = head
    let length = 0

    while (pointer?.val != null) {
        pointer = pointer.next
        length++
    }

    pointer = head
    let pos = 0
    while (pos < Math.floor(length / 2) -1) {
        pointer = pointer.next
        pos++
    }


    pointer.next = (pointer?.next?.next === undefined ? null : pointer?.next?.next)
    return head as ListNode
};
// @lc code=end

