/*
 * @lc app=leetcode id=283 lang=typescript
 *
 * [283] Move Zeroes
 */

// @lc code=start
/**
 Do not return anything, modify nums in-place instead.
 */
 function moveZeroes(nums: number[]): void {
    let offset = 0, i = 0, lenght = nums.length
    while(i < lenght- offset){
        if (nums[i] == 0) {
            nums.push(nums.splice(i, 1)[0])
            offset++
        }
        else {
            i++
        }    
    }  
};
// @lc code=end

