function minOperations(nums: number[]): number {
    let frequency = getFrequency(nums)

    let total = 0

    for (const key in frequency) {
        let elem = frequency[key]

        if (elem == 1) {
            return -1
        }

        total += Math.floor(elem / 3) // use 3 operation 2 time

        if (elem % 3 != 0){
            total++
        }

    }

    return total
};


function getFrequency(str: number[]): { [id: number]: number; } { //
    var frequency : {[id: number]: number} = {}
    
    for (const char of str) {
        if (frequency[char] == undefined) {
            frequency[char] = 1
        }
        else {
            frequency[char] ++;
        }
        
    }
    return frequency
}