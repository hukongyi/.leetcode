#
# @lc app=leetcode.cn id=187 lang=python3
# @lcpr version=30105
#
# [187] 重复的DNA序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans_out = list()
        ans = dict()
        for i in range(len(s)-10+1):
            ans[s[i:i+10]] = ans.get(s[i:i+10],0)+1
            if ans[s[i:i+10]]==2:
                ans_out.append(s[i:i+10])

        return ans_out
# @lc code=end



#
# @lcpr case=start
# "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"\n
# @lcpr case=end

# @lcpr case=start
# "AAAAAAAAAAAAA"\n
# @lcpr case=end

#

