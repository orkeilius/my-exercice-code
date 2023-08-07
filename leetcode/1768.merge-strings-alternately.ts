/*
 * @lc app=leetcode id=1768 lang=typescript
 *
 * [1768] Merge Strings Alternately
 */

// @lc code=start
function mergeAlternately(word1: string, word2: string): string {
    let i = 0
    let out = ""
    let max = Math.max(word1.length, word2.length)
    while (i < max) {
        if (i < word1.length) {
            out = out + word1[i]
        }
        if (i < word2.length) {
            out = out + word2[i]
        }
        i ++
    }
    return out
};
// @lc code=end

