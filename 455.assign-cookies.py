#
# @lc app=leetcode.cn id=455 lang=python3
# @lcpr version=30112
#
# [455] 分发饼干
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        num = 0
        while i < len(s) and j < len(g):
            if g[j] <= s[i]:
                j += 1
                i += 1
                num += 1
            else:
                i+=1
        return num

# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n[1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[1,2,3]\n
# @lcpr case=end

#
