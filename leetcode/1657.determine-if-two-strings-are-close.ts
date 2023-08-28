/*
 * @lc app=leetcode id=1657 lang=typescript
 *
 * [1657] Determine if Two Strings Are Close
 */

// @lc code=start
function closeStrings(word1: string, word2: string): boolean {

    if (word1.length != word2.length) {
        return false
    }
    let count1 = new Map(), count2 = new Map()

    for (let i = 0; i < word1.length; i++) {
        count1.set(word1[i], 1 + ( count1.has(word1[i]) ? count1.get(word1[i]) : 0 )); 
        count2.set(word2[i], 1 + ( count2.has(word2[i]) ? count2.get(word2[i]) : 0 ));  
    }
    

    let keys1 = Array.from(count1.keys()), keys2 = new Set(count2.keys())
    for (let i = 0; i < keys1.length; i++) {
        if (!keys2.has( keys1[i] )) {
            return false
        }
    }


    
    let arr1 = Array.from(count1.values()).sort(), arr2 = Array.from(count2.values()).sort()
    console.log(arr1,arr2)
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) {
            return false
        }
    }
    return true
};
// @lc code=end

