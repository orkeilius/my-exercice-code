/*
 * @lc app=leetcode id=1614 lang=java
 *
 * [1614] Maximum Nesting Depth of the Parentheses
 */

// @lc code=start
class Solution {
    public int maxDepth(String text) {
        int maxDepth = 0;
        int current = 0;
        for (char elem : text.toCharArray()) {
            if (elem == '(') {
                current++;
                maxDepth = Integer.max(current, maxDepth);
            }
            if (elem == ')') {
                current--;
            }
            
        }    
    
        return maxDepth;
    }
}
// @lc code=end

