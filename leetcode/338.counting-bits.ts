/*
 * @lc app=leetcode id=338 lang=typescript
 *
 * [338] Counting Bits
 */

// @lc code=start
function countBits(n: number): number[] {
    const out = [0]

    for (let i = 1; i <= n; i++) {
        out.push(out[i >> 1] + (i & 1));
    }

    return out;
}
// @lc code=end

