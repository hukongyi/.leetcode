#
# @lc app=leetcode.cn id=135 lang=python3
# @lcpr version=30112
#
# [135] 分发糖果
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                ans[i] = ans[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                ans[i] = max(ans[i + 1] + 1, ans[i])
        return sum(ans)


# @lc code=end


#
# @lcpr case=start
# [1,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,4,5,2]\n
# @lcpr case=end


#
