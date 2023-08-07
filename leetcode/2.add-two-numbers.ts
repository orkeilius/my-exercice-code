/*
 * @lc app=leetcode id=2 lang=typescript
 *
 * [2] Add Two Numbers
 */
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

// @lc code=start

function addTwoNumbers(
    l1: ListNode | null,
    l2: ListNode | null
): ListNode | null {
    let mem: number = 0;
    let result = new Array();
    while (l1 != null || l2 != null || mem != 0) {
        let val = (l1?.val ?? 0) + (l2?.val ?? 0) + mem;

        mem = Math.floor(val / 10);
        result.push(val % 10);

        l1 = l1?.next ?? null;
        l2 = l2?.next ?? null;
    }

    let out: ListNode | null = null;
    for (let i = result.length - 1; i >= 0; i--) {
        out = new ListNode(result[i], out);
    }

    return out;
}
// @lc code=end
