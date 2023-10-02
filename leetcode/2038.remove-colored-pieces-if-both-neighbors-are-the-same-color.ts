/*
 * @lc app=leetcode id=2038 lang=typescript
 *
 * [2038] Remove Colored Pieces if Both Neighbors are the Same Color
 */

// @lc code=start
function winnerOfGame(colors: string): boolean {
    var elem = { A: 0, B: 0 }
    
    for (let i = 1; i < colors.length - 1; i++) {
        if (colors[i - 1] === colors[i] && colors[i] === colors[i + 1]) {
            elem[colors[i]] += 1
        }
    }
    return elem['A'] > elem['B']
};
// @lc code=end

