/*
 * @lc app=leetcode id=11 lang=typescript
 *
 * [11] Container With Most Water
 */

// @lc code=start
function maxArea(height: number[]): number {
    let low = 0, high = height.length - 1
    let best = 0
    
    while (low < high) {
        let lowestHeight = Math.min(height[low], height[high])
        best = Math.max(best, lowestHeight * (high - low))


        if (height[low] == lowestHeight) {
            while (height[low] <= lowestHeight && low < high) {
                low++
            }
        }
        else {
            while (height[high] <= lowestHeight && low < high) {
                high--
            }
        }
    }
    return best
};
// @lc code=end

