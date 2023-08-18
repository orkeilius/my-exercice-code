/*
 * @lc app=leetcode id=1071 lang=typescript
 *
 * [1071] Greatest Common Divisor of Strings
 */

// @lc code=start
function gcdOfStrings(str1: string, str2: string): string {
    // get gcd
    if (str1 + str2 !== str2 + str1){
        return ""
    }
    let a = Math.max(str1.length, str2.length);
    let b = Math.min(str1.length, str2.length);
    let gcd = 0;
    while (true) {
        if (b == 0) {
            gcd = a;
            break;
        }
        a %= b;
        if (a == 0) {
            gcd = b;
            break;
        }
        b %= a;
    }
    return str1.slice(0, gcd);
}
// @lc code=end
