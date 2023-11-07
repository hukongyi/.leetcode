#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30105
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = list()
        p_counts = [0]*26
        for t in p:
            p_counts[ord(t)-ord("a")] += 1
        s_counts = [0]*26
        l = 0
        for r in range(len(p)):
            s_counts[ord(s[r])-ord("a")] += 1
        if s_counts == p_counts:
            ans.append(l)
        for r in range(len(p), len(s)):
            s_counts[ord(s[r])-ord("a")] += 1
            s_counts[ord(s[l])-ord("a")] -= 1
            l += 1
            if s_counts == p_counts:
                ans.append(l)
        return ans

        # @lc code=end

        #
        # @lcpr case=start
        # "cbaebabacd"\n"abc"\n
        # @lcpr case=end

        # @lcpr case=start
        # "abab"\n"ab"\n
        # @lcpr case=end

        #
