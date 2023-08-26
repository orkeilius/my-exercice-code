/*
 * @lc app=leetcode id=1207 lang=typescript
 *
 * [1207] Unique Number of Occurrences
 */

// @lc code=start
function uniqueOccurrences(arr: number[]): boolean {
    let occurance = new Map()

    for (let i = 0; i < arr.length; i++) {
        if (occurance.has(arr[i])) {
            occurance.set(arr[i], 1 + occurance.get(arr[i]) ); 
        }
        else {
            occurance.set(arr[i],1)
        }
    }
    let values = new Set(Array.from(occurance.values()))
    return occurance.size == values.size
};
// @lc code=end

