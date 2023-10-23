#
# @lc app=leetcode.cn id=771 lang=python3
# @lcpr version=30102
#
# [771] 宝石与石头
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = set(list(jewels))
        for stone in list(stones):
            if stone in jewels:
                count += 1
        return count
# @lc code=end


#
# @lcpr case=start
# "aA"\n"aAAbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "z"\n"ZZ"\n
# @lcpr case=end

#
