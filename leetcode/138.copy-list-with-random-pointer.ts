/*
 * @lc app=leetcode id=138 lang=typescript
 *
 * [138] Copy List with Random Pointer
 */


class Node {
    val: number
    next: Node | null
    random: Node | null
    constructor(val?: number, next?: Node, random?: Node) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
        this.random = (random===undefined ? null : random)
    }
}

// @lc code=start

function copyRandomList(head: Node | null): Node | null {
    if (head == null) { return head }
    
    let hash = new Map()

    let point = head
    while (point ) {
        hash.set(point,new Node(point.val,point.next,point.random))
        point = point.next
    }

    hash.forEach(elem => {
        if (elem.next) elem.next = hash.get(elem?.next)
        if (elem.random) elem.random = hash.get(elem?.random)
    });

    return hash.get(head)
};
// @lc code=end

