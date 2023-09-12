/*
 * @lc app=leetcode id=841 lang=typescript
 *
 * [841] Keys and Rooms
 */

// @lc code=start
function canVisitAllRooms(rooms: number[][]): boolean {
    let visited = new Set([0])
    let queue = [0]

    while (queue.length != 0) {
        let room = queue.shift() as number

        rooms[room].forEach(elem => {
            if (!visited.has(elem)) {
                queue.push(elem)
                visited.add(elem)
            }
        });
    }
    return visited.size == rooms.length
};
// @lc code=end

