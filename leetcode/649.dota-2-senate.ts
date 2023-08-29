/*
 * @lc app=leetcode id=649 lang=typescript
 *
 * [649] Dota2 Senate
 */

// @lc code=start
function predictPartyVictory(senate: string): string {
    let queue = senate.split("")
    let kickR = 0, kickD = 0
 
    while (queue.length > 1 && Math.max(kickD,kickR) < queue.length) {
        if (queue[0] == "R") {
            if (kickR != 0) {
                kickR--
            }
            else {
                kickD++
                queue.push("R")
            }
        }
        else {
            if (kickD != 0) {
                kickD--
            }
            else {
                kickR++
                queue.push("D")
            }
        }
        queue.shift()
    }
    return queue[0] == "R" ? "Radiant" : "Dire"
};
// @lc code=end

