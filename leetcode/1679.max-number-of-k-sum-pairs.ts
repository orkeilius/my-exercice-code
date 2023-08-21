/*
 * @lc app=leetcode id=1679 lang=typescript
 *
 * [1679] Max Number of K-Sum Pairs
 */

// @lc code=start
function maxOperations(nums: number[], k: number): number {
    nums.sort((a, b) => a - b)
    let low = 0, high = nums.length - 1
    let total = 0
    while (low < high) {
        while (nums[low] + nums[high] == k && low < high) {
            total++
            low++
            high--
        }

        if (nums[low] + nums[high]  < k) {
                low++
        }
        else {
                high--
        }
    }
    return total
};
// @lc code=end

