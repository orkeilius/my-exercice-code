/*
 * @lc app=leetcode id=328 lang=typescript
 *
 * [328] Odd Even Linked List
 */
class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}
//@lc code=start
function oddEvenList(head: ListNode | null): ListNode | null {
    if(!head || !head.next){
        return head
    }

    let even = new ListNode(head.next.val)
    let odd = new ListNode(head.val)
    let oddStart = odd
    let evenStart = even

    let isOdd = true
    head = head.next.next
    while (head != null) {
        if (isOdd) {
            odd.next = new ListNode(head.val)
            odd = odd.next
        }
        else {
            even.next = new ListNode(head.val)
            even = even.next
        }
        head = head.next
        isOdd = !isOdd
    }

    odd.next = evenStart
    return oddStart
};
// @lc code=end

