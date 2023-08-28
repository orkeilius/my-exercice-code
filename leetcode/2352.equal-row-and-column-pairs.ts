/*
 * @lc app=leetcode id=2352 lang=typescript
 *
 * [2352] Equal Row and Column Pairs
 */

// @lc code=start
function equalPairs(grid: number[][]): number {

    let row = new Map()
    for (let i = 0; i < grid.length; i++) {
        let string = JSON.stringify(grid[i])
        row.set(string, 1 + ( row.has(string) ? row.get(string) : 0 )); 
        
    }
    let total = 0

    for (let i = 0; i < grid.length; i++) {
        let column = grid.map(e => {return e[i]}) 

        if (row.has(JSON.stringify(column))){
            total += row.get(JSON.stringify(column))
        }
    }
    return total
};
// @lc code=end

