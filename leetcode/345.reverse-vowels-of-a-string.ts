/*
 * @lc app=leetcode id=345 lang=typescript
 *
 * [345] Reverse Vowels of a String
 */

// @lc code=start
let vowelsList = ["a","e","u","i","o"]
function reverseVowels(s: string): string {

    let Vowels:string[] = []
    for (let i = 0; i < s.length; i++) {
        if (vowelsList.includes( s.charAt(i).toLowerCase())) {
            Vowels.push(s.charAt(i))
        }
    }
    for (let i = 0; i < s.length; i++) {
        if (vowelsList.includes( s.charAt(i).toLowerCase())) {
            s= s.slice(0, i) + Vowels.pop() + s.slice(i+1);
        }
    }
    return s

};
// @lc code=end

