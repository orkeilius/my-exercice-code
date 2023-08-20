/*
 * @lc app=leetcode id=443 lang=typescript
 *
 * [443] String Compression
 */

function compress(chars: string[]): number {
    let out :string[] = []
    let i = 0
    while (i < chars.length) {
        let value = chars[i]
        let count = 0
        while (chars[i] == value) {
            count++
            i++
        }
        out.push(value)
        if(count > 1){
            out.push( ...count.toString().split(""))
        }      
    }

    // chars = out | don't work because the test is rigged and test the referenced data in the list instead of the list itself
    for (let i = 0; i < chars.length; i++) {
        chars[i] = out[i];
    }
    chars = chars.slice(0,out.length)
    return chars.length
}

// @lc code=end