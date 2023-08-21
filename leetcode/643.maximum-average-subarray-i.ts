/*
 * @lc app=leetcode id=643 lang=typescript
 *
 * [643] Maximum Average Subarray I
 */

// @lc code=start
function findMaxAverage(nums: number[], k: number): number {
    let total = 0 
    for (let i = 0; i < k; i++) {
        total += nums[i];
        
    }
    let best = total
    for (let i = k; i < nums.length; i++) {
        total += nums[i] - nums[i - k]
        best = Math.max(best, total)
    }
    return best / k
};
// @lc code=end

