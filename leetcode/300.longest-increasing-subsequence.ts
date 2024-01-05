function lengthOfLIS(nums: number[]): number {
    
    let scoreList: number[] = [0]
    let best: number = -1

    for (let elem = 0; elem < nums.length; elem++) {

        // find nearest smaller number
        let bestPrevious = 0
        for (var previous = 0; previous < elem; previous++) {
            if (nums[elem] > nums[previous] && scoreList[previous + 1] > scoreList[bestPrevious]) {
                bestPrevious = previous + 1
            }
        }

        var score = scoreList[bestPrevious] + 1

        if (score > best) {
            best = score
        }
        scoreList.push(score)

        
    }
    return best    
};