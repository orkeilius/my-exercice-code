/*
 * @lc app=leetcode id=1732 lang=typescript
 *
 * [1732] Find the Highest Altitude
 */

// @lc code=start
function largestAltitude(gain: number[]): number {
    let alt = 0, best = 0
    while(gain.length != 0){
        alt += gain.shift()
        best = Math.max(best,alt)   
    }
    return best
}
// @lc code=end

