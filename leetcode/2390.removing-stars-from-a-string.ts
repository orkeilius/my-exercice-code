/*
 * @lc app=leetcode id=2390 lang=typescript
 *
 * [2390] Removing Stars From a String
 */

// @lc code=start
function removeStars(s: string): string {
    let list :string[] = []
    for (let i = 0; i < s.length; i++) {
        if (s[i] == "*") {
            list.pop()
        }
        else {
            list.push(s[i])
        }
    }
    return list.join("")
};
// @lc code=end

