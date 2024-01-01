#
# @lc app=leetcode.cn id=763 lang=python3
# @lcpr version=30112
#
# [763] 划分字母区间
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        print(len(s))
        last_appear = dict()
        for i, s_i in enumerate(s[::-1]):
            if s_i not in last_appear:
                last_appear[s_i] = len(s) - 1 - i
        ans = list()
        tmp = 0
        for i, s_i in enumerate(s):
            tmp = max(tmp, last_appear[s_i])
            if i == tmp:
                ans.append(tmp + 1 - sum(ans))
        return ans


# @lc code=end


#
# @lcpr case=start
# "ababcbacadefegdehijhklij"\n
# @lcpr case=end

# @lcpr case=start
# "eccbbbbdec"\n
# @lcpr case=end

#
