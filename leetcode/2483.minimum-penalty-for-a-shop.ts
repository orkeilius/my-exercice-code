/*
 * @lc app=leetcode id=2483 lang=typescript
 *
 * [2483] Minimum Penalty for a Shop
 */

// @lc code=start
function bestClosingTime(customers: string): number {
    let best = { score: 0, hour: 0 }
    let score = 0
    for (let i = 0; i < customers.length; i++) {
        score += customers[i] == 'Y' ? 1 : -1

        if (best.score < score) {
            best = {score: score,hour:i+1}
        }
    }
    return best.hour
};
// @lc code=end

