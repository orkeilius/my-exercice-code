/*
 * @lc app=leetcode id=678 lang=java
 *
 * [678] Valid Parenthesis String
 */

// @lc code=start
class Solution {
    public boolean checkValidString(String s) {
        int depthMin = 0;
        int depthMax = 0;

        for (char elem : s.toCharArray()) {
            if (elem == '(') {
                depthMin++;
                depthMax++;
            } else if (elem == ')') {
                depthMin = Math.max(0, depthMin - 1);
                depthMax--;
            } else {
                depthMin = Math.max(0, depthMin - 1);
                depthMax++;
            }

            if (depthMax < 0) {
                return false;
            }
        }
        return depthMin == 0;
    }
}
// @lc code=end

