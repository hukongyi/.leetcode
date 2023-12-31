#
# @lc app=leetcode.cn id=2706 lang=python3
# @lcpr version=30112
#
# [2706] 购买两块巧克力
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_2 = [-i for i in prices[:2]]
        heapq.heapify(min_2)
        for i in prices[2:]:
            heapq.heappush(min_2, -i)
            heapq.heappop(min_2)
        sum_2 = sum(min_2)
        if money+sum_2 < 0:
            return money
        else:
            return money+sum_2

# @lc code=end


#
# @lcpr case=start
# [1,2,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3]\n3\n
# @lcpr case=end

#
