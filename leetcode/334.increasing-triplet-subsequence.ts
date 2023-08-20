/*
 * @lc app=leetcode id=334 lang=typescript
 *
 * [334] Increasing Triplet Subsequence
 */

// @lc code=start
function increasingTriplet(nums: number[]): boolean {
    let lowestA = nums[0]
    let lowestB = 2 ** 32
    for (let i = 0; i < nums.length - 2; i++) {
        lowestA = Math.min(lowestA, nums[i])
        
        if (lowestA < nums[i + 1]) {
            lowestB = Math.min(lowestB, nums[i + 1])
        }

        if (lowestB < nums[i + 2]) {
            return true
        }
    }

    return false
};
// @lc code=end

