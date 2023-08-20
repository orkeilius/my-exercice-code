/*
 * @lc app=leetcode id=392 lang=typescript
 *
 * [392] Is Subsequence
 */

// @lc code=start
function isSubsequence(s: string, t: string): boolean {
    let iSub = 0
    let iText = 0
    if(s == ""){return true}
    while (iText < t.length) {
        if (t[iText] == s[iSub]) {
            iSub++
            if (iSub == s.length) {
                return true
            }
        }        
        iText++
    }
    return false
};
// @lc code=end

