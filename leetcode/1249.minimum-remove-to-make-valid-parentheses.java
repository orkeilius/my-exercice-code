/*
 * @lc app=leetcode id=1249 lang=java
 *
 * [1249] Minimum Remove to Make Valid Parentheses
 */
import java.util.*;

// @lc code=start

class Solution {
    public String minRemoveToMakeValid(String s) {
    
        Stack<Integer> posParenthese = new Stack<Integer>();

        for (int i = 0; i < s.length(); i++) {
            char elem = s.charAt(i);
            if (elem == '('){
                posParenthese.push(i);
            } else if(elem == ')'){
                if(posParenthese.isEmpty()){
                    s = removeElem(s,i);
                    i--;
                }else{
                    posParenthese.pop();
                }
            }
        }

        int i = 0;
        for (Integer elem : posParenthese) {
            s = removeElem(s, elem - i);
            i ++;
        }
        return s;
    }
    public String removeElem(String text, int pos) {
        if (pos == text.length() -1){
            return text.substring(0, pos);
        }
        return text.substring(0, pos) + text.substring(pos + 1);
    }
}
// @lc code=end

