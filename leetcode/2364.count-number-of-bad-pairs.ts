function countBadPairs(nums: number[]): number {
    var frequency = new Map<number, number>()

    for (let num = 0; num < nums.length; num++) {
        let val = nums[num] - num
        if (!frequency.has(val)) {
            frequency.set(val, 1)
        }
        else {
            frequency.set(val,frequency.get(val) + 1)
        }
    }

    var nbGood = 0
    
    for (const elem of frequency.values()) {
        nbGood += elem**2
    }
    return ((nums.length ** 2) - nbGood) / 2
};