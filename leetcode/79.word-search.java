/*
 * @lc app=leetcode id=79 lang=java
 *
 * [79] Word Search
 */

import java.util.*;
// @lc code=start


class Solution {

    public boolean exist(char[][] board, String word) {
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int x = 0; x < board.length; x++) {
            for (int y = 0; y < board[0].length; y++) {
                if (board[x][y] == word.charAt(0)) {
                    if (searchNode(new int[] { x, y }, word,board,visited,0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    private boolean searchNode(int[] pos, String word,char[][] board,boolean[][] visited,int i) {
        if(board.length <= pos[0] || pos[0] < 0 || board[0].length <= pos[1] || pos[1] < 0){
            return false;
        }
        if (word.charAt(i) != board[pos[0]][pos[1]]) {
            return false;
        }
        if (visited[pos[0]][pos[1]] == true) {
            return false;
        }
        
        if (word.length() == i + 1) {
            return true;
        }

        visited[pos[0]][pos[1]] = true;
        if (
            searchNode(new int[] { pos[0] +1, pos[1] }, word,board,visited,i+1) ||
            searchNode(new int[] { pos[0] -1, pos[1] }, word,board,visited,i+1) ||
            searchNode(new int[] { pos[0], pos[1] +1 }, word,board,visited,i+1) ||
            searchNode(new int[] { pos[0], pos[1] -1 }, word,board,visited,i+1)
            ){
                return true;
            }

        visited[pos[0]][pos[1]] = false;
        return false;
    }
    
}
// @lc code=end

