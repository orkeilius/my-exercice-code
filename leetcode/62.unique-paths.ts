/*
 * @lc app=leetcode id=62 lang=typescript
 *
 * [62] Unique Paths
 */

// @lc code=start
function uniquePaths(m: number, n: number): number {
    let previousLine: number[] = new Array(n + 1).fill(0)
    let line: number[] = new Array(n + 1)
    line[0]=1
    for (let i = 0; i < m; i++) {
        for (let j = 1; j <= n; j++) {
            line[j] = line[j -1] + previousLine[j]
        }        
        previousLine = line        
    }
    return previousLine[n - 1]
};
// @lc code=end

