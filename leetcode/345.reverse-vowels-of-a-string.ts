/*
 * @lc app=leetcode id=345 lang=typescript
 *
 * [345] Reverse Vowels of a String
 */

// @lc code=start
let vowelsList = new Set("aeuioAEUIO".split(""))
function reverseVowels(s: string): string {

    let low = 0
    let high = s.length - 1
    let text: string[] = s.split("")
    while (low < high) {
        while (!vowelsList.has( text[low]) && low < high) {
            low++
        }
        while (!vowelsList.has( text[high]) && low < high) {
            high--
        }
        // console.log(low,high)
        let temp = text[low]
        text[low] = text[high] 
        text[high] = temp
        
        low++
        high--
    }
    return text.join("")
};
// @lc code=end