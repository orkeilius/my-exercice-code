/*
 * @lc app=leetcode id=1700 lang=java
 *
 * [1700] Number of Students Unable to Eat Lunch
 */

import java.util.*;
// @lc code=start


class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Queue<Integer> queue = new LinkedList<Integer>();
        for (int student : students)
            queue.offer(student);
        Stack<Integer> stack = new Stack<Integer>();
        for (int i =  sandwiches.length -1; i >= 0; i--) {
            stack.push(sandwiches[i]);
        }

        int nbReject = 0;
        while (nbReject < queue.size() && queue.size() != 0) {
            Integer currentStudent = queue.poll();
            Integer currentSandwiche = stack.peek();

            if (currentSandwiche != currentStudent) {
                queue.offer(currentStudent);
                nbReject++;
            } else {
                stack.pop();
                nbReject = 0;
            }
        }
        return queue.size();
    }
}
// @lc code=end

