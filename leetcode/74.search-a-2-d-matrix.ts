/*
 * @lc app=leetcode id=74 lang=typescript
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
function searchMatrix(matrix: number[][], target: number): boolean {

    let y = 1
    let x = 0
    while (y < matrix.length){
        if (matrix[y][0] > target) {
            break
        }  
        y += 1
        
    }
    y -= 1
    while (x <  matrix[y].length){
        let e = matrix[y][x]
        if (e === target) {
            return true
        }
        else if(e > target) {
            break
        }  
        x++
    } 
    return false

};
// @lc code=end