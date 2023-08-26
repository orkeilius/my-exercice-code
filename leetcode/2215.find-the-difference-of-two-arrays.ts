/*
 * @lc app=leetcode id=2215 lang=typescript
 *
 * [2215] Find the Difference of Two Arrays
 */

// @lc code=start
function findDifference(nums1: number[], nums2: number[]): number[][] {
    let out  = [new Set<number>(),new Set<number>()]

    let set1 = new Set(nums2)
    for (let i = 0; i < nums1.length; i++) {
        if (!set1.has(nums1[i])) {
            out[0].add(nums1[i])
        }
    }

    let set2 = new Set(nums1)
    for (let i = 0; i < nums2.length; i++) {
        if (!set2.has(nums2[i])) {
            out[1].add(nums2[i])
        }
    }

    return [Array.from( out[0]),Array.from(out[1])]
};
// @lc code=end

