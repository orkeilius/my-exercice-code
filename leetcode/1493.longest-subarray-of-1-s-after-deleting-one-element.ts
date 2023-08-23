/*
 * @lc app=leetcode id=1493 lang=typescript
 *
 * [1493] Longest Subarray of 1's After Deleting One Element
 */

// @lc code=start
function longestSubarray(nums: number[]): number {
    let low = 0
    let best = 0
    let k = 0
    for (let high = 0; high < nums.length; high++) {
        if (nums[high] == 0) {
            if (++k > 1 ) {
                while (nums[low] == 1) {
                    low++
                }
                low++
                k--
            }
        }
        if(best < high - low ){
            best = high - low  
        } 
    }
    return best
};
// @lc code=end

