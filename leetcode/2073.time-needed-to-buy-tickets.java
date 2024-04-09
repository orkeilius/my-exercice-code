/*
 * @lc app=leetcode id=2073 lang=java
 *
 * [2073] Time Needed to Buy Tickets
 */

import java.util.*;

// @lc code=start

import java.util.Queue;

class Solution {

    public int timeRequiredToBuy(int[] tickets, int k) {

        int time = 0;
        int pos = 0;
        while (tickets[k] != 0) {
            if (tickets[pos] >= 1) {
                tickets[pos]--;
                time++;
            }
            pos = (pos + 1) % tickets.length;
        }
        return time;
    }


    public int timeRequiredToBuyOld(int[] tickets, int k) {
        
        Queue<int[]> queue = new LinkedList<int[]>();
        for (int i = 0; i < tickets.length; i++) {
            queue.add(new int[] { tickets[i],i });
        }

        int time = 0;
        while (queue.size() > 0) {
            time++;
            int[] elem = queue.poll();
            if (elem[0] > 1) {
                elem[0] -= 1; 
                queue.offer(elem);
            }
            else if (elem[1] == k) {
                return time;
            }
        }
        return -1;
    }
}
// @lc code=end

