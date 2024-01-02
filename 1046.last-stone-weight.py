#
# @lc app=leetcode.cn id=1046 lang=python3
# @lcpr version=30112
#
# [1046] 最后一块石头的重量
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-2]=stones[-1]-stones[-2]
                stones.pop()
                stones.sort()
        if len(stones)>0:
            return stones[0]
        else:
            return 0
# @lc code=end



#
# @lcpr case=start
# [2,7,4,1,8,1]\n
# @lcpr case=end

#

