#
# @lc app=leetcode.cn id=2707 lang=python3
# @lcpr version=30112
#
# [2707] 字符串中的额外字符
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        letterdict = dict()
        for l in dictionary:
            letterdict[l] = 1
            for i in range(1, len(l)):
                letterdict[l[i:]] = letterdict.get(l[i:],0)
        dp = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            dpv = [dp[i-1]+1]
            for j in range(i-1,-1,-1):
                if s[j:i] in letterdict:
                    if letterdict[s[j:i]] ==1:
                        dpv.append(dp[j])
                else:
                    break
            dp[i] = min(dpv)
        return dp[-1]


# @lc code=end


#
# @lcpr case=start
# "leetscode"\n["leet","code","leetcode"]\n
# @lcpr case=end

# @lcpr case=start
# "sayhelloworld"\n["hello","world"]\n
# @lcpr case=end

#
