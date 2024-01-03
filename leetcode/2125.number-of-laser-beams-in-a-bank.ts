/*
 * @lc app=leetcode id=2125 lang=typescript
 *
 * [2125] Number of Laser Beams in a Bank
 */

// @lc code=start
function numberOfBeams(bank: string[]): number {

    let previous = 0
    let total = 0

    for (const row of bank) {
        let nbDevice: number = row.match(/1/g)?.length
        if (nbDevice == undefined) {
            continue
        }

        total += nbDevice * previous
        previous = nbDevice
    } 
    return total
};
// @lc code=end

