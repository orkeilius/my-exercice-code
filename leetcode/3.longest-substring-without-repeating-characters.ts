/*
 * @lc app=leetcode id=3 lang=typescript
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
function lengthOfLongestSubstring(s: string): number {
    let start : number = 0;
    let best: number = 0;
    let value: string[] = [];

    for (let i = 0; i < s.length; i++) {
        const elem = s[i];


        if (s.slice(start,i - 1).includes(elem)) {
            start += s.slice(start,i - 1).indexOf(elem)
        }

        best = Math.max(best, i - start)
        
    }

    return best
};
// @lc code=end

