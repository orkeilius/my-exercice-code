/*
 * @lc app=leetcode id=238 lang=typescript
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
function productExceptSelf(nums: number[]): number[] {

    let list = new Array(nums.length).fill(1)
    let pre = 1,suf = 1
    for (let i = 0; i < nums.length; i++) {
        list[i] *= pre
        list[nums.length - i -1] *= suf
        // console.log(list,pre,suf,)
        pre *= nums[i]
        suf *= nums[nums.length - i -1]   
    }
    return list
};
// @lc code=end

