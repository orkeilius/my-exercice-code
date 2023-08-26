/*
 * @lc app=leetcode id=724 lang=typescript
 *
 * [724] Find Pivot Index
 */

// @lc code=start
function pivotIndex(nums: number[]): number {
    let total = 0
    let target = nums.reduce((partialSum, a) => partialSum + a, 0) ;
    for (let i = 0; i < nums.length; i++) {
        if (total * 2 + nums[i] == target) {
            return i
        } 
        total += nums[i];
    } 
    return -1
};
// @lc code=end

