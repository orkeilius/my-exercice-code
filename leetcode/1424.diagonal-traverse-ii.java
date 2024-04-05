/*
 * @lc app=leetcode id=1424 lang=java
 *
 * [1424] Diagonal Traverse II
 */

import java.util.*;
// @lc code=start


class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        ArrayList<Integer> out = new ArrayList<Integer>();

        Queue<int[]> queue = new LinkedList<int[]>();
        queue.offer(new int[]{0,0});

        while(!queue.isEmpty()){
            int[] elem = queue.poll();

            out.add(nums.get(elem[0]).get(elem[1]));

            if (elem[1] == 0 && elem[0] < nums.size() - 1) {
                queue.offer(new int[]{elem[0] + 1,0});
            }
            if (elem[1] < nums.get(elem[0]).size() - 1) {
                queue.offer(new int[]{elem[0],elem[1] + 1});
            }
        }
        
        return convertIntegerToInt(out);
    }
    
    public int[] convertIntegerToInt(ArrayList<Integer> l) {
        int[] out = new int[l.size()];
        int i = 0;
        for (int elem : l) {
            out[i++] = elem;
        }
        return out;
    }
}
// @lc code=end

