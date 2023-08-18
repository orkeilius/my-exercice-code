// @lc code=start
function search(nums: number[], target: number): number {

    //find rotation
    let start = 0
    let end = nums.length - 1
    let mid = 0
    while (start <= end) {
        mid = Math.floor((start + end) / 2)
        // console.log(start,mid,end)
        if (nums[mid] == target) {
            return mid
        }

        if (nums[start] <= nums[mid]) {
            if (nums[start] <= target && target < nums[mid]) {
                end = mid - 1
            }
            else {
                start = mid + 1
            }
        }
        else {
            if (nums[mid] < target && target <= nums[end]) {
                start = mid + 1
            }
            else {
                end = mid - 1
            }
        }
    }
    return -1
};