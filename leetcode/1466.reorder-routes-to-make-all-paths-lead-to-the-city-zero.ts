/*
 * @lc app=leetcode id=1466 lang=typescript
 *
 * [1466] Reorder Routes to Make All Paths Lead to the City Zero
 */

// @lc code=start
function minReorder(n: number, connections: number[][]): number {
    let links: number[][][] = []
    for (let i = 0; i < n; i++) {
        links.push([]);
        
    }
    
    for (let i = 0; i < connections.length; i++) {
        links[connections[i][0]].push([connections[i][1],1])
        links[connections[i][1]].push([connections[i][0],0])
    }


    let nbRedirect = 0
    let queue = [[0, 0]]
    
    while (queue.length != 0) {
        let elem = queue.pop() as number[]
        for (let link of links[elem[0]]) {
            if (link[0] != elem[1]) {
                nbRedirect += link[1]
                queue.push([link[0],elem[0]])
            }
        }
    }
    return nbRedirect
};
// @lc code=end

