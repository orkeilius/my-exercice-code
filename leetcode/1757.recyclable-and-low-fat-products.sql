--
-- @lc app=leetcode id=1757 lang=mysql
--
-- [1757] Recyclable and Low Fat Products
--

-- @lc code=start
SELECT product_id 
FROM Products 
WHERE low_fats = 'Y'AND recyclable = 'Y'

-- @lc code=end

