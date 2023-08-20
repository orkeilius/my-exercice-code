/*
 * @lc app=leetcode id=392 lang=typescript
 *
 * [392] Is Subsequence
 */

// @lc code=start
function isSubsequence(s: string, t: string): boolean {
    let iSub = 0
    let iText = 0
    while (iText < t.length && iSub < s.length) {
        if (t[iText] == s[iSub]) {
            iSub++
        }        
        iText++
    }
    return iSub == s.length
};
// @lc code=end

