/*
 * @lc app=leetcode id=394 lang=typescript
 *
 * [394] Decode String
 */

// @lc code=start
function decodeString(s: string): string {
    let stack = [ { number: 0 , text: "" } ]
    for (let i = 0; i < s.length; i++) {
        if ("1234567890".includes(s[i])) {
            stack[0].number = stack[0].number * 10 + parseInt(s[i]) 
        }
        else if (s[i] == "[") {
            stack.unshift({ number: 0 , text: "" })
        }
        else if (s[i] == "]") {
            stack[1] ={
                text : stack[1].text + stack[0].text.repeat(stack[1].number) ,
                number : 0
            } 
            stack.shift()
        }
        else {
            stack[0].text = stack[0].text + s[i]
        }
    }
    return stack[0].text
};
// @lc code=end

