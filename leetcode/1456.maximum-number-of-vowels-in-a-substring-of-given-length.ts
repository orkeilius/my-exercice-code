/*
 * @lc app=leetcode id=1456 lang=typescript
 *
 * [1456] Maximum Number of Vowels in a Substring of Given Length
 */

// @lc code=start
const Vowels = ["a","e","i","o","u"]

function maxVowels(s: string, k: number): number {
    let total = 0 
    for (let i = 0; i < k; i++) {
        total += Vowels.includes(s[i]) && 1        
    }
    let best = total
    for (let i = k; i < s.length; i++) {
        total += Vowels.includes(s[i]) && 1 
        total -= Vowels.includes(s[i - k]) && 1
        best = Math.max(best, total)
    }
    return best
};
// @lc code=end

