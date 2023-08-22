/*
 * @lc app=leetcode id=168 lang=typescript
 *
 * [168] Excel Sheet Column Title
 */

// @lc code=start
function convertToTitle(columnNumber: number): string {
    let out :String[] = []
    while (columnNumber > 0 ) {
        out.unshift( String.fromCharCode(65 + (columnNumber - 1 )% 26) )
        columnNumber = Math.floor((columnNumber -1) / 26)
    }
    return out.join("")
};
// @lc code=end

