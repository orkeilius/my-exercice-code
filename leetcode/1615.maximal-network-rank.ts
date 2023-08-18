/*
 * @lc app=leetcode id=1615 lang=typescript
 *
 * [1615] Maximal Network Rank
 */

// @lc code=start
function maximalNetworkRank(n: number, roads: number[][]): number {
    
    let citys:number[][] = []
    
    for (let i = 0; i < n; i++) {
        citys.push(Array());
    }
    while (roads.length !== 0) {
        citys[roads[0][0]].push(roads[0][1])
        citys[roads[0][1]].push(roads[0][0])
        roads.shift()
    }
    let best = -1

    for (let a = 0; a < citys.length; a++) {
        for (let b = a + 1; b < citys.length; b++) {
            best = Math.max(citys[a].length + citys[b].length - (citys[a].includes(b)? 1 : 0), best )
            //console.log(a,b,best)
        } 
    }
    return best
};
// @lc code=end

