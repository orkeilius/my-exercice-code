/*
 * @lc app=leetcode id=118 lang=typescript
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
function generate(numRows: number): number[][] {
    let list : number[][] = []

    for (let i = 1; i <= numRows; i++) {
        list.push([])

        for (let j = 0; j < i; j++) {

            if (j == 0  || j == i - 1) {
                list[list.length -1 ].push(1)
            }
            else {
                list[list.length -1 ].push( 
                   list[list.length -2 ][j] + 
                   list[list.length -2 ][j - 1]   
                ) 
            }
        }
        
    }

    return list
};

// @lc code=end

