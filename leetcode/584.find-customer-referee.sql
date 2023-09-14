--
-- @lc app=leetcode id=584 lang=mysql
--
-- [584] Find Customer Referee
--

-- @lc code=start
select name from Customer where  IFNULL(referee_id, -1) != 2
-- @lc code=end

