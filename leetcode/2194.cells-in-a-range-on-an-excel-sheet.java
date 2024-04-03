/*
 * @lc app=leetcode id=2194 lang=java
 *
 * [2194] Cells in a Range on an Excel Sheet
 */

import java.util.*;

// @lc code=start

class Solution {

    public List<String> cellsInRange(String s) {
        int startY = s.charAt(0);
        int startX = s.charAt(1);

        int endY = s.charAt(3);
        int endX = s.charAt(4);

        List<String> out = new ArrayList<String>();

        for (int y = startY; y <= endY; y++) {
            for (int x = startX; x <= endX; x++) {
                out.add(
                    new String(new char[] {(char) y,(char) x }));
                System.out.println("e");
            }
        }
        return out;
    }
}
// @lc code=end
