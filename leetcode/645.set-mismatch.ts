function findErrorNums(nums: number[]): number[] {
    var found = new Set()
    var ouput = [0, 0]
    
    for (const num of nums) {
        if (found.has(num)) {
            ouput[0] = num
        }
        else {
            found.add(num)
        }
    }

    for (let i = 0; i < nums.length; i++) {
        if (!found.has(i)) {
           ouput[1] = i
       } 
    }

    return ouput
    
};