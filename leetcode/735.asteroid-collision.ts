/*
 * @lc app=leetcode id=735 lang=typescript
 *
 * [735] Asteroid Collision
 */

// @lc code=start
function asteroidCollision(asteroids: number[]): number[] {
    let stack: number[] = []
    for (let i = 0; i < asteroids.length; i++) {
        if (asteroids[i] > 0 || stack[stack.length -1]  < 0) {
            stack.push(asteroids[i])
        }
        else {
            while (stack[stack.length -1] < Math.abs(asteroids[i]) && stack.length != 0 && stack[stack.length -1] > 0) {
                stack.pop()
            }
            if (stack.length == 0 || stack[stack.length -1]  < 0) {
                stack.push(asteroids[i])
            }
            else if (stack[stack.length -1]   == Math.abs(asteroids[i])) {
                stack.pop()
            }
        }
    }
    return stack
};
// @lc code=end

