#
# @lc app=leetcode.cn id=274 lang=python3
# @lcpr version=30103
#
# [274] H 指数
#

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = [0]*len(citations)
        for i in citations:
            for j in range(min(i, len(ans))):
                ans[j] += 1
        for i in range(len(ans)):
            if i+1>ans[i]:
                return i
        return i+1
# @lc code=end



#
# @lcpr case=start
# [3,0,6,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1]\n
# @lcpr case=end

#

