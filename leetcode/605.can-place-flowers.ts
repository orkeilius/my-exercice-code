/*
 * @lc app=leetcode id=605 lang=typescript
 *
 * [605] Can Place Flowers
 */

// @lc code=start
function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    if (n == 0) {
        return true
    }
    
    let nb = 0
    while (nb < flowerbed.length){
        if (flowerbed[nb -1] !== 1 && flowerbed[nb] !== 1 && flowerbed[nb +1] !== 1) {
            n--
            flowerbed[nb] == 1
            if (n == 0) {
                return true
            }
            nb++
        }
        nb++
    }

    return false

};
// @lc code=end

