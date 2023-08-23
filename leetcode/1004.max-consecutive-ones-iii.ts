/*
 * @lc app=leetcode id=1004 lang=typescript
 *
 * [1004] Max Consecutive Ones III
 */

// @lc code=start
function longestOnes(nums: number[], k: number): number {
    let low = 0
    let best = 0
    for (let high = 0; high < nums.length; high++) {
        if (nums[high] == 0) {
            if (--k < 0 ) {
                while (nums[low] == 1) {
                    low++
                }
                low++
                k++
            }
        }
        if(best <= high - low + 1){
            best = high - low + 1
        } 
    }
    return best
};
// @lc code=end

