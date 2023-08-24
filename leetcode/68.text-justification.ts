/*
 * @lc app=leetcode id=68 lang=typescript
 *
 * [68] Text Justification
 */

// @lc code=start
function fullJustify(words: string[], maxWidth: number): string[] {
    let out: string[] = []
    let low = 0, high = 0
    let space = 0
    while (high < words.length) {
        let width = -1
        while (high < words.length) {
            if (width + words[high].length + 1 > maxWidth) {
                break
            }
            width+= words[high].length + 1
            high++
        }

        if (high <words.length) {
            space = (high-low) + (maxWidth - width) -1
        }
        else{
            space = (high-low) -1
        }

        let line= ""
        for (let i = low; i < high; i++) {
            line = line + words[i] + " ".repeat(Math.ceil(space / Math.max(1, high - i -1)) )
            space -= Math.ceil(space / Math.max(1, high - i -1))        
        }
        
        out.push(line + " ".repeat(maxWidth - line.length))
        low = high
    }
    return out
};
// @lc code=end

