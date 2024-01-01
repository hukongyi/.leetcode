#
# @lc app=leetcode.cn id=134 lang=python3
# @lcpr version=30112
#
# [134] 加油站
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        ans = [0]
        for i in range(len(gas)):
            ans.append(ans[i] + gas[i] - cost[i])
        return ans.index(min(ans))


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n[3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#
